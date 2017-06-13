#!flask/bin/python
from flask.ext.httpauth import HTTPBasicAuth
from flask import Flask, jsonify, request, make_response
import subprocess

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
        if username == 'jy':
                return 'python'
        return None

@auth.error_handler
def unauthorized():
        return make_response(jsonify({'error': 'Unauthorized Access'}), 403)

child = subprocess.Popen('cat bridge.json',stdout=subprocess.PIPE,shell=True)
output = child.communicate()[0]
tasks = output

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
@auth.login_required
def create_loop():
	cloop = 'sudo vppctl loopback create-interface'
	subprocess.call(cloop,shell=True)
	return ''

@app.route('/todo/api/v1.0/tasks', methods=['DELETE'])
@auth.login_required
def delete_loop():
	if not request.json or not 'Name' in request.json:
		abort(400)
	task = {'Name': request.json['Name']}
	loopint = str(request.json['Name'])
	dloop = 'sudo vppctl loopback delete-interface intfc %s' % (loopint)
	subprocess.call(dloop,shell=True)
	return ''

@app.route('/todo/api/v1.0/tasks', methods=['PUT'])
@auth.login_required
def update_bridge():
	if not request.json or not 'id' in request.json:
		abort(400)
	task = {'id': request.json['id']}
	bridge = str(request.json['id'])
	upbridge = 'sudo vppctl set bridge-domain forward %s' % (bridge)
	subprocess.call(upbridge,shell=True)
	#update json file
	update = "python read.py"
	subprocess.call(update,shell=True)
	#update flask
	nchild = subprocess.Popen('cat bridge.json',stdout=subprocess.PIPE,shell=True)
	noutput = nchild.communicate()[0]
	tasks = noutput
	return tasks

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
	#update json file
        update = "python read.py"
        subprocess.call(update,shell=True)
        #update flask
        nchild = subprocess.Popen('cat bridge.json',stdout=subprocess.PIPE,shell=True)
        noutput = nchild.communicate()[0]
        tasks = noutput
	return tasks
if __name__ == '__main__':
	app.run(debug=True)

