"""
A wiki API that returns the summary of an article as a JSON {'searchTerm': 'summary'}
endpoint:  url/?search=searchTerm
"""


from flask import Flask, jsonify, request
import wikipedia


app = Flask(__name__)

# allows web app to make cross origin requests
@app.after_request
def cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


# http GET request route
# endpoint:  url/?search=searchTerm
@app.route('/')
def get():
    searchTerm = request.args.get('search')
    
    try:
        return jsonify({searchTerm: wikipedia.summary(searchTerm)})
    except:
        # error
        return 'Remove any space or symbol from search term, or try a different search.'



if __name__ == '__main__':
    app.run(debug=True)