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




#Xiu QI 2nd set CRUD

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





#Jing Ming 1st CRUD


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

        nsub= subprocess.Popen('sudo vppctl show bridge-domain',stdout=subprocess.PIPE,shell=True)
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





#Jian Yuan 1st set CRUD

@app.route('/todo/jianyuan/createloop', methods=['POST'])
@auth.login_required
def create_loop():
	cloop = 'sudo vppctl loopback create-interface'
	subprocess.call(cloop,shell=True)

	#display loopback interfaces
	nchild = subprocess.Popen('sudo vppctl show int',stdout=subprocess.PIPE,shell=True)
	noutput = nchild.communicate()[0]
	showinterfaces = noutput
	return showinterfaces




@app.route('/todo/jianyuan/showbridgedomains', methods=['GET'])
@auth.login_required
def get_bridgedomain():
	#update json file
        update = "python combined.py"
        subprocess.call(update,shell=True)
        #update flask
        nchild = subprocess.Popen('cat bridge.json',stdout=subprocess.PIPE,shell=True)
        noutput = nchild.communicate()[0]
        showbridgedomains = noutput
	return showbridgedomains




@app.route('/todo/jianyuan/updateforward', methods=['PUT'])
@auth.login_required
def update_forward():
	if not request.json or not 'id' in request.json:
		abort(400)
	task = {
		'id': request.json['id'],
		'state': request.json['state']
	}
	bridge = str(request.json['id'])
	state = str(request.json['state'])
	if state == "enable":
		state = ""
	upbridge = 'sudo vppctl set bridge-domain forward %s %s' % (bridge, state)
	subprocess.call(upbridge,shell=True)
	#update json file
	update = "python combined.py"
	subprocess.call(update,shell=True)
	#update flask
	nchild = subprocess.Popen('cat bridge.json',stdout=subprocess.PIPE,shell=True)
	noutput = nchild.communicate()[0]
	displaybridge = noutput
	return displaybridge




@app.route('/todo/jianyuan/delloop', methods=['DELETE'])
@auth.login_required
def delete_loop():
	if not request.json or not 'Name' in request.json:
		abort(400)
	task = {'Name': request.json['Name']}
	loopint = str(request.json['Name'])
	dloop = 'sudo vppctl loopback delete-interface intfc %s' % (loopint)
	subprocess.call(dloop,shell=True)
	#display loopback interfaces
        nchild = subprocess.Popen('sudo vppctl show int',stdout=subprocess.PIPE,shell=True)
        noutput = nchild.communicate()[0]
        showinterfaces = noutput
        return showinterfaces







#Jian Yuan 2nd set CRUD

@app.route('/todo/jianyuan2/createvxlan', methods=['POST'])
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
	#display all vxlan tunnels
	nchild = subprocess.Popen('sudo vppctl show vxlan tunnel',stdout=subprocess.PIPE,shell=True)
	noutput = nchild.communicate()[0]
	showvxlantunnels = noutput
	return showvxlantunnels



@app.route('/todo/jianyuan2/showhardwares', methods=['GET'])
@auth.login_required
def get_showhardwares():
	#update json file
        update = "python combined.py"
        subprocess.call(update,shell=True)
        #update flask
        nchild = subprocess.Popen('cat show.json',stdout=subprocess.PIPE,shell=True)
        noutput = nchild.communicate()[0]
        showhardwares = noutput
        return showhardwares



@app.route('/todo/jianyuan2/updateterm', methods=['PUT'])
@auth.login_required
def update_term():
        if not request.json or not 'id' in request.json:
                abort(400)
        task = {'id': request.json['id'], 'state': request.json['state']}
        bridge = str(request.json['id'])
	state = str(request.json['state'])
	if state == "enable":
		state = ""
        upbridge = 'sudo vppctl set bridge-domain arp term %s %s' % (bridge, state)
        subprocess.call(upbridge,shell=True)
	#update json file
        update = "python combined.py"
        subprocess.call(update,shell=True)
        #update flask
        nchild = subprocess.Popen('cat bridge.json',stdout=subprocess.PIPE,shell=True)
        noutput = nchild.communicate()[0]
        displaybridge = noutput
        return displaybridge




@app.route('/todo/jianyuan2/delvxlan', methods=['DELETE'])
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
	#display all vxlan tunnels
        nchild = subprocess.Popen('sudo vppctl show vxlan tunnel',stdout=subprocess.PIPE,shell=True)
        noutput = nchild.communicate()[0]
        showvxlantunnels = noutput
        return showvxlantunnels






#Function for update (bridge domains) including all types of bridge-domain: Done by Xiu Qi for the team
@app.route('/todo/Team5/updatebridgedomain', methods=['UPDATE'])
@auth.login_required
def update_bridgedomain():

        if not request.json:
                abort(400)

        task = {
                'ID': request.json['ID'],
		'learn': request.json['learn'],
		'forward': request.json['forward'],
		'uuflood': request.json['uuflood'],
		'flood': request.json['flood'],
                'arpterm': request.json['arpterm']
        }

        intid = str(request.json['ID'])
	learnstate = str(request.json['learn'])
	forwardstate = str(request.json['forward'])
	uufloodstate = str(request.json['uuflood'])
	floodstate = str(request.json['flood'])
        arptermstate = str(request.json['arpterm'])

	#learn
        if learnstate == "enable":
                learnstate = ""
		updatelearn = 'sudo vppctl set bridge-domain learn %s %s' % (intid,learnstate)
		subprocess.call(updatelearn, stdout=subprocess.PIPE, shell = True)
	elif learnstate == "disable":
		updatelearn = 'sudo vppctl set bridge-domain learn %s %s' %  (intid,learnstate)
		subprocess.call(updatelearn, stdout=subprocess.PIPE, shell = True)

	#forward
	if forwardstate == "enable":
		forwardstate = ""
		updateforward = 'sudo vppctl set bridge-domain forward %s %s' % (intid,forwardstate)
		subprocess.call(updateforward, stdout=subprocess.PIPE, shell = True)
	elif forwardstate == "disable":
		updateforward = 'sudo vppctl set bridge-domain forward %s %s' % (intid,forwardstate)
                subprocess.call(updateforward, stdout=subprocess.PIPE, shell = True)

	#uu-flood
	if uufloodstate == "enable":
		uufloodstate = ""
		updateuuflood = 'sudo vppctl set bridge-domain uu-flood %s %s' % (intid,uufloodstate)
		subprocess.call(updateuuflood, stdout=subprocess.PIPE, shell = True)
	elif uufloodstate == "disable":
		updateuuflood = 'sudo vppctl set bridge-domain uu-flood %s %s' % (intid,uufloodstate)
                subprocess.call(updateuuflood, stdout=subprocess.PIPE, shell = True)


	#flood
	if floodstate == "enable":
		floodstate = ""
		updateflood = 'sudo vppctl set bridge-domain flood %s %s' % (intid,floodstate)
		subprocess.call(updateflood, stdout=subprocess.PIPE, shell = True)
	elif floodstate == "disable":
		updateflood = 'sudo vppctl set bridge-domain flood %s %s' % (intid,floodstate)
                subprocess.call(updateflood, stdout=subprocess.PIPE, shell = True)


	#arpterm
	if arptermstate == "enable":
		arptermstate = ""
		updatearpterm = 'sudo vppctl set bridge-domain arp term %s %s' % (intid,arptermstate)
		subprocess.call(updatearpterm, stdout=subprocess.PIPE, shell = True)
	elif arptermstate == "disable":
		updatearpterm = 'sudo vppctl set bridge-domain arp term %s %s' % (intid,arptermstate)
		subprocess.call(updatearpterm, stdout=subprocess.PIPE, shell = True)


        #Display effect of the commands
        cps = subprocess.Popen('sudo vppctl show bridge-domain', stdout=subprocess.PIPE, shell = True)
        ot = cps.communicate()[0]
        displaybridgedomain = ot

        return displaybridgedomain

#end of combined update bridge-domain commands




if __name__ == '__main__':
    app.run(debug=True)
