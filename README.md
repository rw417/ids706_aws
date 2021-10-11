# ids706_aws
This is a repo for using AWS for the course IDS706 - Data Engineering

# Project 1 - FastAPI Microservice Random Text Generator
[![Python CI to AWS](https://github.com/rw417/ids706_aws/actions/workflows/project1.yml/badge.svg)](https://github.com/rw417/ids706_aws/actions/workflows/project1.yml)  
This is a straighforward microservice created using FastAPI and hosted on AWS App Runner.  
It supports 3 use cases:
1. The homepage returns a welcome message in the form a a json payload
2. /add/{num1}/{num2} returns the sum of {num1} and {num2} in the form of a json payload
3. /multiply/{num1}/{num2} returns the product of {num1} and {num2} in the form of a json payload

To use the microservice, visit [this link](https://ujrgewf3fm.us-east-2.awsapprunner.com/).

Documentation of the API can be found at [this link](https://ujrgewf3fm.us-east-2.awsapprunner.com/docs).
