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

child = subprocess.Popen('cat show.json',stdout=subprocess.PIPE,shell=True)
output = child.communicate()[0]
tasks = output

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
@auth.login_required
def create_vxlan():
	if not request.json:
                abort(400)
	task = {'src': request.json['src'], 'dst': request.json['dst'], 'vni': request.json['vni']}
	src = str(request.json['src'])
	dst = str(request.json['dst'])
	vni = str(request.json['vni'])
	cvxlan = 'sudo vppctl create vxlan tunnel src %s dst %s vni %s' % (src, dst, vni)
	subprocess.call(cvxlan,shell=True)
	return ''

@app.route('/todo/api/v1.0/tasks', methods=['DELETE'])
@auth.login_required
def delete_vxlan():
	if not request.json:
                abort(400)
        task = {'src': request.json['src'], 'dst': request.json['dst'], 'vni': request.json['vni']}
        src = str(request.json['src'])
        dst = str(request.json['dst'])
        vni = str(request.json['vni'])
        cvxlan = 'sudo vppctl create vxlan tunnel src %s dst %s vni %s del' % (src, dst, vni)
        subprocess.call(cvxlan,shell=True)
        return ''

@app.route('/todo/api/v1.0/tasks', methods=['PUT'])
@auth.login_required
def update_bridge():
        if not request.json or not 'id' in request.json:
                abort(400)
        task = {'id': request.json['id']}
        bridge = str(request.json['id'])
        upbridge = 'sudo vppctl set bridge-domain arp term %s' % (bridge)
        subprocess.call(upbridge,shell=True)
	return ''

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
	#update json file
        update = "python read2.py"
        subprocess.call(update,shell=True)
        #update flask
        nchild = subprocess.Popen('cat show.json',stdout=subprocess.PIPE,shell=True)
        noutput = nchild.communicate()[0]
        tasks = noutput
        return tasks
if __name__ == '__main__':
        app.run(debug=True)
