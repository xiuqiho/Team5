#!flask/bin/python 
from flask_httpauth import HTTPBasicAuth
from flask import Flask, jsonify, abort, request, make_response
import subprocess

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
        if username == 'team5':
                return 'sti'
        return None

@auth.error_handler
def unauthorized():
        return make_response(jsonify({'error': 'Unauthorized Access'}), 403)


#Xiu Qi 1st set of CRUD

@app.route('/todo/xiuqi/createint', methods=['POST'])
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
        updatejsonfile = "python combined.py"
        subprocess.call(updatejsonfile,shell = True)

        #Update flask
        ncps = subprocess.Popen('cat showintresult.json',stdout=subprocess.PIPE,shell=True)
        noutput = ncps.communicate()[0]
        showint = noutput

        return showint


@app.route('/todo/xiuqi/showint', methods=['GET'])
@auth.login_required
def get_tasks():

        #Update json file
        updatejsonfile = "python combined.py"
        subprocess.call(updatejsonfile,shell=True)

        #Update flask
        ncps = subprocess.Popen('cat showintresult.json',stdout=subprocess.PIPE,shell=True)
        noutput = ncps.communicate()[0]
        showint = noutput

        return showint


@app.route('/todo/xiuqi/updateint', methods=['UPDATE'])
@auth.login_required
def update_task():

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

	#Update json file
        updatejsonfile = "python combined.py"
        subprocess.call(updatejsonfile,shell=True)

        #Update flask
        ncps = subprocess.Popen('cat showintresult.json',stdout=subprocess.PIPE,shell=True)
        noutput = ncps.communicate()[0]
        showint = noutput

        return showint


@app.route('/todo/xiuqi/deleteint', methods=['DELETE'])
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
        updatejsonfile = "python combined.py"
        subprocess.call(updatejsonfile,shell=True)

        #Update flask
        ncps = subprocess.Popen('cat showintresult.json',stdout=subprocess.PIPE,shell=True)
        noutput = ncps.communicate()[0]
        showint = noutput

        return showint

if __name__ == '__main__':
    app.run(debug=True)

