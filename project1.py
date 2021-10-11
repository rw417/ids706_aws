"""Doc string"""
import uvicorn
import spacy
import re
import markovify
import nltk
from nltk.corpus import gutenberg
import en_core_web_sm
import warnings
from fastapi import FastAPI

warnings.filterwarnings("ignore")
nltk.download("gutenberg")


# import novels as text objects
hamlet = gutenberg.raw("shakespeare-hamlet.txt")
macbeth = gutenberg.raw("shakespeare-macbeth.txt")
caesar = gutenberg.raw("shakespeare-caesar.txt")


# utility function for text cleaning
def text_cleaner(text):
    """"""
    text = re.sub(r"--", " ", text)
    text = re.sub("[\\[].*?[\\]]", "", text)
    text = re.sub(r"(\b|\s+\-?|^\-?)(\d+|\d*\.\d+)\b", "", text)
    text = " ".join(text.split())
    return text


# remove chapter indicator
hamlet = re.sub(r"Chapter \d+", "", hamlet)
macbeth = re.sub(r"Chapter \d+", "", macbeth)
caesar = re.sub(r"Chapter \d+", "", caesar)
# apply cleaning function to corpus
hamlet = text_cleaner(hamlet)
caesar = text_cleaner(caesar)
macbeth = text_cleaner(macbeth)


# parse cleaned novels
nlp = spacy.load("en_core_web_sm")
hamlet_doc = nlp(hamlet)
macbeth_doc = nlp(macbeth)
caesar_doc = nlp(caesar)


# Now that our texts are cleaned and processed, we can create sentences
# and combine our documents.
hamlet_sents = " ".join(
    [sent.text for sent in hamlet_doc.sents if len(sent.text) > 1])
macbeth_sents = " ".join(
    [sent.text for sent in macbeth_doc.sents if len(sent.text) > 1]
)
caesar_sents = " ".join(
    [sent.text for sent in caesar_doc.sents if len(sent.text) > 1])
shakespeare_sents = hamlet_sents + macbeth_sents + caesar_sents


# create text generator using markovify
# generator_1 = markovify.Text(shakespeare_sents, state_size=3)


# next we will use spacy's part of speech to generate more legible text
class POSifiedText(markovify.Text):
    """"""
    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence


# Call the class on our text
generator_2 = POSifiedText(shakespeare_sents, state_size=4)


app = FastAPI()


@app.get("/")
async def root():
    """"""
    return {"Welcome!":
            """This is a Shakespear-style random text generator.
            Please enter the number of sentences you'd like to generate as integers."""
           }


@app.get("/{n}")
async def genSentences(n: int):
    """"""
    s = ""
    for i in range(n):
        currentSentence = generator_2.make_sentence()
        while currentSentence is None:
            currentSentence = generator_2.make_sentence()
        newStr = " ".join((s, currentSentence))
        s = newStr

    return {"Please enjoy your Shakespearisc novella": s}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
