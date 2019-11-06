from flask import Flask, request, current_app, jsonify
from flask_cors import CORS

from recommendation import r

DEBUG = True
app = Flask(__name__, static_url_path='/static')
CORS(app)


@app.route('/result', methods=['GET'])
def songs():
    if request.method == 'GET':
        data = (request.args.to_dict())
        number = data['number']
        mood = data['mood']
        d=(r(number, mood))
        # print(d)
        res={'res':r(number, mood)}
        return jsonify(res)


if __name__ == "__main__":
    app.run()
