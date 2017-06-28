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


#Xiu Qi 2nd set CRUD


@app.route('/todo/xiuqi2/createdhcp', methods=['POST'])
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

	#Display effect of the commands
	cps = subprocess.Popen('sudo vppctl show dhcp client', stdout=subprocess.PIPE, shell = True)
	ot = cps.communicate()[0]
	displaydhcp = ot

	return displaydhcp



@app.route('/todo/xiuqi2/showbuffer', methods=['GET'])
@auth.login_required
def get_buffer():

	#Update json file
        updatejsonfile = "python combined.py"
        subprocess.call(updatejsonfile,shell=True)

        #Update flask
        ncps = subprocess.Popen('cat showbuffresult.json',stdout=subprocess.PIPE,shell=True)
        noutput = ncps.communicate()[0]
        showbuff = noutput

        return showbuff





@app.route('/todo/xiuqi2/updateuuflood', methods=['UPDATE'])
@auth.login_required
def update_uuflood():

        if not request.json or not 'State' in request.json:
                abort(400)

        task = {
                'ID': request.json['ID'],
                'State': request.json['State']
        }

        intid = str(request.json['ID'])
        uufloodstate = str(request.json['State'])

	if uufloodstate == "enable":
		uufloodstate = ""
		updateuuflood = 'sudo vppctl set bridge-domain uu-flood %s %s' % (intid,uufloodstate)
		subprocess.call(updateuuflood, stdout=subprocess.PIPE, shell = True)
	elif uufloodstate == "disable":
		updateuuflood = 'sudo vppctl set bridge-domain uu-flood %s %s' % (intid,uufloodstate)
                subprocess.call(updateuuflood, stdout=subprocess.PIPE, shell = True)

	#Display effect of the commands
        cps = subprocess.Popen('sudo vppctl show bridge-domain', stdout=subprocess.PIPE, shell = True)
        ot = cps.communicate()[0]
        displaybridgedomain = ot

        return displaybridgedomain




@app.route('/todo/xiuqi2/deldhcp', methods=['DELETE'])
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

	#Display effect of the commands
        cps = subprocess.Popen('sudo vppctl show dhcp client', stdout=subprocess.PIPE, shell = True)
        ot = cps.communicate()[0]
        displaydhcp = ot

        return displaydhcp


if __name__ == '__main__':
    app.run(debug=True)
