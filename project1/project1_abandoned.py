from fastapi import FastAPI
import uvicorn
import pandas as pd
import nltk


def prefixes(output, n):
    if n == 1:  # if unigram, return an empty list as prefix
        return []
    if n-1 >= len(output):
        return output
    else:
        return output[-(n-1):]


def getDenom(ntokens, corpus):
    n = len(ntokens)
    denom = 0
    for i in range(len(corpus)-n):
        nTokenChunk = corpus[i:(i+n)]
        if ntokens == nTokenChunk:
            denom += 1
            pass
        pass
    return denom


def getNumer(ntokens, corpus):
    numerators = {}
    n = len(ntokens)
    for i in range(len(corpus)-n-1):
        nTokenChunk = corpus[i:(i+n)]
        if ntokens == nTokenChunk:
            nextToken = corpus[i+n]
            numerators.setdefault(nextToken, [0, i])
            numerators[nextToken][0] += 1
            pass
        pass
    numerators = dict(
        sorted(numerators.items(), key=lambda item: (-item[1][0], item[1][1])))
    return numerators


def buildDistribution(numer, denom):
    dist = pd.DataFrame.from_dict(numer, orient='index', columns=[
                                  'count', 'firstAppearance'])
    dist = dist / denom
    return dist


def stupidBackoff(output, n, numer, denom, corpus):
    while denom == 0 or len(numer) == 0:
        n = n - 1
        ntokens = prefixes(output, n)
        denom = getDenom(ntokens, corpus)
        numer = getNumer(ntokens, corpus)
    return buildDistribution(numer, denom)


def findNextToken(possibleTokens, deterministic):
    if deterministic == True:
        return possibleTokens.index[0]
    if deterministic == False:
        return possibleTokens.sample(weights='count').index[0]


def getSentence(ipt):
    s = ipt.split('_')
    return s


app = FastAPI()


@app.get("/")
async def root():
    return {"""This is a text generator.\nPlease enter a few words after the slash in the url.\nUse underscores (_) instead of spaces to separate the words."""}


@app.get("/{input}")
async def finish_sentence(input: str):
    sentence = getSentence(input)
    n = 3
    corpus = nltk.corpus.gutenberg.raw('austen-sense.txt')
    corpus = nltk.word_tokenize(corpus.lower())
    deterministic = False
    
    output = sentence.copy()
    while (len(output) < 20) and (output[-1] not in [',', '.', '?', '!']):
        ntokens = prefixes(output, n)
        denom = getDenom(ntokens, corpus)
        numer = getNumer(ntokens, corpus)
        possibleTokens = stupidBackoff(output, n, numer, denom, corpus)
        foundNextToken = findNextToken(possibleTokens, deterministic)
        output.append(foundNextToken)
    
    return {"Your generated sentence is": output}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
