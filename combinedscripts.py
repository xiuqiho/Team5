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


#showint (Xiu Qi)
spcs = subprocess.Popen('cat showintresult.json',stdout=subprocess.PIPE,shell=True)
result = spcs.communicate()[0]
showint = result

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




#showbuffer (Xiu Qi)
spcs = subprocess.Popen('cat showbuffresult.json', stdout=subprocess.PIPE, shell = True)
result = spcs.communicate()[0]
showbuffer = result


@app.route('/todo/xiuqi/createdhcp', methods=['POST'])
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



@app.route('/todo/xiuqi/showbuffer', methods=['GET'])
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





@app.route('/todo/xiuqi/updateuuflood', methods=['UPDATE'])
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

	if intstate == "enable":
		intstate = ""


        update = 'sudo vppctl set bridge-domain uu-flood %s %s' % (intid,intstate)
        subprocess.call(update, stdout=subprocess.PIPE, shell = True)

	#Display effect of the commands
        cps = subprocess.Popen('sudo vppctl show bridge domain', stdout=subprocess.PIPE, shell = True)
        ot = cps.communicate()[0]
        displaybridgedomain = ot

        return displaybridgedomain




@app.route('/todo/xiuqi/deldhcp', methods=['DELETE'])
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





#showiparp (Jing Ming)
sp= subprocess.Popen('cat setip.json', stdout=subprocess.PIPE,shell=True)
output = sp.communicate()[0]
showiparp = output



@app.route('/todo/jingming/setiparp', methods=['POST'])
@auth.login_required
def create_iparp():

        task = {
                'Flags': request.json['Flags'],
                'IP4': request.json['IP4'],
                'Interface': request.json['Interface'],
                'Ethernet': request.json['Ethernet']
        }

        flag = str(request.json['Flags'])
        ipaddr = str(request.json['IP4'])
        intf = str(request.json['Interface'])
        ent = str(request.json['Ethernet'])

        put= "sudo vppctl set ip arp %s %s %s %s" % (flag,intf, ipaddr, ent)
        sp2= subprocess.Popen(put,shell=True,stdout=subprocess.PIPE)
        noutput= sp2.communicate()[0]

        update= "python combined.py"
        subprocess.call(update,shell=True)

        nsub= subprocess.Popen('cat setip.json',stdout=subprocess.PIPE,shell=True)
        newoutput = nsub.communicate()[0]
        showiparp = newoutput

        return showiparp




@app.route('/todo/jingming/showiparp', methods=['GET'])
@auth.login_required
def get_iparp():

        update= "python combined.py"
        subprocess.call(update,shell=True)

        nsub= subprocess.Popen('cat setip.json',stdout=subprocess.PIPE,shell=True)
        newoutput = nsub.communicate()[0]
        showiparp = newoutput

        return showiparp




@app.route('/todo/jingming/updatelearn', methods=['PUT'])
@auth.login_required
def update_learn():

        task = {
                'ID': request.json['ID'],
                'State': request.json['State']
        }


        ID = str(request.json['ID'])
        state = str(request.json['State'])

	if state == "enable":
                state = ""

        result = "sudo vppctl set bridge-domain learn %s %s" % (ID, state)
        subproc = subprocess.Popen(result,shell=True,stdout=subprocess.PIPE)
        oput= subproc.communicate()[0]

	update= "python combined.py"
        subprocess.call(update,shell=True)

        nsub= subprocess.Popen('sudo vppctl show bridge domain',stdout=subprocess.PIPE,shell=True)
        newoutput = nsub.communicate()[0]
        showbridgedomain = newoutput

        return showbridgedomain




@app.route('/todo/jingming/deleteiparp', methods=['DELETE'])
@auth.login_required
def delete_iparp():


        task = {
                'Flags': request.json['Flags'],
                'IP4': request.json['IP4'],
		'Interface': request.json['Interface'],
                'Ethernet': request.json['Ethernet']
        }

        flag = str(request.json['Flags'])
        ipaddr = str(request.json['IP4'])
	intf = str(request.json['Interface'])
        ent = str(request.json['Ethernet'])


        put= "sudo vppctl set ip arp %s delete %s %s %s" % (flag,intf, ipaddr, ent)
	sp2= subprocess.Popen(put,shell=True,stdout=subprocess.PIPE)
        noutput= sp2.communicate()[0]

        update= "python combined.py"
        subprocess.call(update,shell=True)

        nsub= subprocess.Popen('cat setip.json',stdout=subprocess.PIPE,shell=True)
        newoutput = nsub.communicate()[0]
        showiparp = newoutput

        return showiparp































if __name__ == '__main__':
    app.run(debug=True)
