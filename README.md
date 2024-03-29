# Hamify

This is the repository for the Hamify (formerly known as DNASB) service created by Gage Christensen for the 2020 UNR ACM Biggest Little Hackathon.

# Reproduction

Building and testing can be reproduced simply by cloning the repository and building the docker image from the dockerfile in transformer/. To reproduce deployment, you would need to duplicate this repository and produce your own credentials. Make a github secret for GCLOUD\_AUTH. This should be a base64 encoded key for a Google Cloud service account. You will also need to have a cloud run service set up prior to deploying the application. You can use one of the demo containers to start with. Once you have your google cloud services set up, edit .github/workflows/ci.yml so that the container is pushed to the right location and deployed to your cloud run service.

## Tools

This a RESTful service made with Python and Flask. `nltk` and `pandas` are used for machine learning and natural language processing techniques.

## Idea

This service will accept a message that would be denoted as spam by a spam filter and replace words in that message with synonyms so that it will be denoted as not-ham. This technique of feeding malicious input to machine learning classifiers in order to trick them is known as "Adversarial Machine Learning." It is a common technique for assessing classifiers used for security, and helps to strengthen these classifiers by producing adversarial examples that the models can then be trained against. 

A lot of research on adversarial spam generation focuses on creating the strongest spam generators. For this project, I decided to take a more interpretable approach so that the project could serve as an educational resource on how spam filters work.

## Progress

Currently, the spam transformer will look through the message and generate similar messages based on synonyms. It will pick the first one that gets past its reference spam filter. For its reference filter, it uses a Naive Bayesian Classifier (see notebook). It is currently able to drop the performance of the filter from 99% to 86%.

In the future I intend to expand the functionality of the tool so that it uses other techniques such as ham word injection and spam word spacing. I then intend to train a reinforcement learning model that picks between these techniques based on certain limitations, to see which techniques perform the best in bypassing spam filters.

## API

You may `POST` to `/spam`, which will return the id of the newly posted spam. If you then `GET` from `/ham/<id>/`, you will receive the ham version of your posted spam.
