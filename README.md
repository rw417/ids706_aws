# ids706_aws
This is a repo for using AWS for the course IDS706 - Data Engineering

# Project 1 - FastAPI Microservice Random Text Generator
[![Python CI to AWS](https://github.com/rw417/ids706_aws/actions/workflows/project1.yml/badge.svg)](https://github.com/rw417/ids706_aws/actions/workflows/project1.yml)  
This is a straighforward microservice created using FastAPI and hosted on AWS App Runner.  
It is a text generator using Markov chains, and it generates Shakespear-style sentences. Enter the number of sentences you'd like to generate as integers after the "/" and you'll get sentences in Shakespear style.

The training corpuses used are Hamlet, MacBeth, and Julius Caesar. The program is adapted from [this article](https://towardsdatascience.com/text-generation-with-markov-chains-an-introduction-to-using-markovify-742e6680dc33).

To use the microservice, visit [this link](https://ujrgewf3fm.us-east-2.awsapprunner.com/).

Documentation of the API can be found at [this link](https://ujrgewf3fm.us-east-2.awsapprunner.com/docs).
