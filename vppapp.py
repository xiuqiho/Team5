#!flask/bin/python
from flask import Flask,jsonify,abort,request,make_response
from flask_httpauth import HTTPBasicAuth
import subprocess

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
        if username == 'jingming':
                return 'sti'
        return None

@auth.error_handler
def unauthorized():
        return make_response(jsonify({'error': 'Unauthorized access'}), 401)


app = Flask(__name__)

sp= subprocess.Popen('cat setip.json', stdout=subprocess.PIPE,shell=True)
output = sp.communicate()[0]

tasks = output


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
        
		update= "python vpp.py"
        subprocess.call(update,shell=True)

        nsub= subprocess.Popen('cat setip.json',stdout=subprocess.PIPE,shell=True)
        newoutput = nsub.communicate()[0]
        tasks = newoutput
		
		return tasks

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
@auth.login_required
def create_tasks():

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

        update= "python vpp.py"
        subprocess.call(update,shell=True)

        nsub= subprocess.Popen('cat setip.json',stdout=subprocess.PIPE,shell=True)
        newoutput = nsub.communicate()[0]
        newtask = newoutput

        return ''
		
@app.route('/todo/api/v1.0/tasks', methods=['DELETE'])
@auth.login_required
def delete_tasks():


        task = {
                'Flags': request.json['Flags'],
                'Interface': request.json['Interface'],
                'IP4': request.json['IP4'],
                'Ethernet': request.json['Ethernet']
        }

        flag = str(request.json['Flags'])
        intf = str(request.json['Interface'])
        ipaddr = str(request.json['IP4'])
        ent = str(request.json['Ethernet'])


        put= "sudo vppctl set ip arp %s delete %s %s %s" % (flag,intf, ipaddr, ent)
        subprocess.call(put,stdout=subprocess.PIPE,shell=True)


        update= "python vpp.py"
        subprocess.call(update,shell=True)



        nsub= subprocess.Popen('cat setip.json',stdout=subprocess.PIPE,shell=True)
        newoutput = nsub.communicate()[0]
        newtask = newoutput

        return ''
		
@app.route('/todo/api/v1.0/tasks', methods=['PUT'])
@auth.login_required
def update_tasks():

        task = {
                'ID': request.json['ID'],
                'LEARN': request.json['LEARN'],
                'DIS': request.json['DIS']
        }


        ID = str(request.json['ID'])
        LEARN = str(request.json['LEARN'])
        DIS = str(request.json['DIS'])
        result = "sudo vppctl set bridge-domain %s %s %s" % (LEARN, ID, DIS)
        subproc = subprocess.Popen(result,shell=True,stdout=subprocess.PIPE)
        oput= subproc.communicate()[0]

        return ''



if __name__ == '__main__':
        app.run(debug=True)