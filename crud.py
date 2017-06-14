#!flask/bin/python 
from flask.ext.httpauth import HTTPBasicAuth
from flask import Flask, jsonify, abort, request, make_response
import subprocess

app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
	if username == 'xiuqi':
		return 'sti'
	return None


@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error': 'Unauthorized Access'}), 403)



spcs = subprocess.Popen('cat showintresult.json',stdout=subprocess.PIPE,shell=True)
result = spcs.communicate()[0]

tasks = result



@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
	#Update json file
	updatejsonfile = "python showint.py"
	subprocess.call(updatejsonfile,shell=True)

	#Update flask
	ncps = subprocess.Popen('cat showintresult.json',stdout=subprocess.PIPE,shell=True)
	noutput = ncps.communicate()[0]
	tasks = noutput
	
	return tasks


@app.route('/todo/api/v1.0/tasks', methods=['DELETE'])
@auth.login_required
def del_task():
	if not request.json or not 'Name' in request.json:
		abort(400)

	task = {
		'Name': request.json['Name']
	}

	host = str(request.json['Name'])
	deletecommand = 'sudo vppctl delete host-interface name %s' % (host)
	subprocess.call(deletecommand,stdout=subprocess.PIPE,shell=True)

	#Update json file
	updatejsonfile = "python showint.py"
	subprocess.call(updatejsonfile,shell=True)

	#Update flask
	ncps = subprocess.Popen('cat showintresult.json',stdout=subprocess.PIPE,shell=True)
	noutput = ncps.communicate()[0]
	tasks = noutput

	return ''

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
@auth.login_required
def create_task():

	if not request.json or not 'Name' in request.json:
		abort(400)

	task = {
		'Name': request.json['Name']
	}

	hostname = str(request.json['Name'])
	addcommand = 'sudo vppctl create host-interface name %s' % (hostname)
	subprocess.call(addcommand,stdout=subprocess.PIPE, shell = True)

	#Update json file
	updatejsonfile = "python showint.py"
	subprocess.call(updatejsonfile,shell = True)

	#Update flask
	ncps = subprocess.Popen('cat showintresult.json',stdout=subprocess.PIPE,shell=True)
	noutput = ncps.communicate()[0]
	tasks = noutput

	return ''


@app.route('/todo/api/v1.0/tasks', methods=['UPDATE'])
@auth.login_required
def delete_task():

	if not request.json or not 'Name' in request.json:
		abort(400)
	if not request.json or not 'State' in request.json:
		abort(400)

	task = {
		'Name': request.json['Name'],
		'State': request.json['State']
	}

	name = str(request.json['Name'])
	state = str(request.json['State'])
	addint = 'sudo vppctl set interface state %s %s' % (name, state)
	subprocess.call(addint, stdout=subprocess.PIPE, shell = True)

	#Update JSON File
	updatejsonfile = "python showint.py"
	subprocess.call(updatejsonfile, shell = True)

	#Update Flask
	npcs = subprocess.Popen('cat showintresult.json', stdout=subprocess.PIPE, shell = True)
	noutput = npcs.communicate()[0]
	tasks = noutput

	return ''


if __name__ == '__main__':
	app.run(debug=True)