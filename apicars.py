from flask import Flask, jsonify
import requests
application = Flask(__name__)

@application.route("/api/getmvplate/<string:plate>",methods=["GET"])
def extractplates(plate):
	data = [('txt', plate),]

	results = requests.post('http://159.203.187.227/ocpu/user/bando/library/mpesaoptim/R/extractplates/json', data=data)
    	return jsonify(results.text)

@application.route("/api/countcars/<string:plate1>/<string:plate2>",methods=["GET"])
def platediffs(plate1,plate2):
	data = [('car1',plate1 ), ('car2', plate2),]

	results = requests.post('http://159.203.187.227/ocpu/user/bando/library/mpesaoptim/R/carbetween/json', data=data)
    	return jsonify(results.text)
    

if __name__ == "__main__":
    application.run(host='0.0.0.0')
