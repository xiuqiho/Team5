#!flask/bin/python
from flask import Flask, jsonify, abort, request
import subprocess

app = Flask(__name__)

spcs = subprocess.Popen('cat showbuffresult.json', stdout=subprocess.PIPE, shell = True)
result = spcs.communicate()[0]

buffer = result

#Read
@app.route('/todo/buffer', methods=['GET'])
def get_tasks():
	return buffer

	
#Create
@app.route('/todo/dhcp', methods=['POST'])
def create_dhcp_client():

	if not request.json or not 'Name' in request.json:
		abort(400)

	task = {
		'Name': request.json['Name']
	}

	intname = str(request.json['Name'])
	add = 'sudo vppctl set dhcp client intfc %s ' % (intname)
	subprocess.call(add, stdout=subprocess.PIPE, shell = True)

	return ''

	
#Delete
@app.route('/todo/dhcp', methods=['DELETE'])
def del_dhcp_client():

        if not request.json or not 'Name' in request.json:
                abort(400)

        task = {
                'Name': request.json['Name']
        }

        intname = str(request.json['Name'])
        add = 'sudo vppctl set dhcp client del intfc %s' % (intname)
        subprocess.call(add, stdout=subprocess.PIPE, shell = True)

        return ''


		
#Update
@app.route('/todo/bridge/domain', methods=['UPDATE'])
def update_bridge_domain():

	if not request.json or not 'State' in request.json:
		abort(400)

	task = {
		'ID': request.json['ID'],
		'State': request.json['State']
	}

	intid = str(request.json['ID'])
	intstate = str(request.json['State'])

	update = 'sudo vppctl set bridge-domain uu-flood %s %s' % (intid,intstate)
	subprocess.call(update, stdout=subprocess.PIPE, shell = True)

	return ''

	
	
	
if __name__ == '__main__':
	app.run(debug=True)