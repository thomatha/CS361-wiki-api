# CS361-wiki API

A microservice implemented with Python's Flask framework.
This API communicates via a http GET request.
The response is a JSON object {'userQueryString': 'the summary of an article on wikipedia'}

Endpoint: url/?search=userQueryString
search is the parameter key
userQueryString is the value being searched for

Example GET request: url/?search=meme
Returned result:
{"meme": ""A meme ( MEEM) is an idea, behavior, or style that spreads by means of imitation from person to person within a culture and often carries symbolic meaning representing a particular phenomenon or theme. A meme acts..."}
