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



spcs = subprocess.Popen('cat showbuffresult.json', stdout=subprocess.PIPE, shell = True)
result = spcs.communicate()[0]

buffer = result



@app.route('/todo/buffer', methods=['GET'])
@auth.login_required
def get_tasks():
	return buffer


@app.route('/todo/dhcp', methods=['POST'])
@auth.login_required
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

@app.route('/todo/dhcp', methods=['DELETE'])
@auth.login_required
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



@app.route('/todo/bridge/domain', methods=['UPDATE'])
@auth.login_required
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