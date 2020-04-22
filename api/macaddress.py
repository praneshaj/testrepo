from flask import request, Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/macaddress', methods=['POST'])
def create_task():
    if not request.json or not 'macaddress' in request.json:
        abort(400)
    output = {
        'macaddress': request.json['macaddress'],
        'companyName': ''
    }
    cname = requests.get("http://api.macvendors.com/"+request.json['macaddress']).text
    output.update(companyName = cname)
    return jsonify({'result': output}), 200

if __name__ == '__main__':
    app.run(debug=True)