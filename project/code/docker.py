# coding=utf-8
import subprocess
import sys
import threading
import os
import argparse
import yaml

def callproc(cmd, ignore_return_code=False):
   print('Running: \n' + cmd + '\n')
   ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
   returncode = ps.wait()
   stdout = ps.communicate()[0]
   if returncode != 0 and not ignore_return_code:
       print >> sys.stderr, ('Error: command "{}" failed: {}'.format(cmd, stdout))
       sys.exit(returncode)
   else:
       return stdout


def docker_instal(hostname):
    cmd =  'curl -sSL https://get.docker.com | sh'
    execssh(hostname, cmd)
    

def execssh(hostname, cmd, username=None):
    if username is None:
        cmd = 'ssh ' + hostname + ' "' + cmd + '"'     
    else:     
        cmd = 'ssh ' + username + '@' + hostname + ' "' + cmd + '"'
    callproc(cmd)
      
def swarm_instal(hostname, hosttyp):
    if hosttyp == "Master":
        swarmcmd = 'sudo docker swarm init'
        execssh(hostname,swarmcmd)
    else:
        joincmd = 'sudo docker swarm join-token worker'
        jointkn = callproc(joincmd)
        testsh = 'ssh ' + hostnm + ' ' + callproc(jointkn)
        callproc(testsh)

def pull():
    nodes = callproc("docker node ls | grep Ready | awk -F'[[:space:]][[:space:]]+' '{print $2}'").rstrip().split('\n')

def instal():
   # step1 = callproc("sudo apt-get update -y")
   # step2 = callproc("sudo apt-get -y install curl")
   # step3 = callproc("sudo apt-get upgrade -y")
   # step4 = callproc("sudo apt-get dist-upgrade -y")
   # step5 = callproc("sudo apt-get -y install raspberrypi-ui-mods")
      
    commands='''
       sudo apt-get update -y
       sudo apt-get -y install curl
       sudo apt-get upgrade -y
       sudo apt-get dist-upgrade -y
       sudo apt-get -y install raspberrypi-ui-mods
       '''
    for line in commands:
         # print (line)
        step=callproc(line)

 # def main(hostnm1, master):
 #   parser = argparse.ArgumentParser()
 #   parser.add_argument("hostnm", help="Enter the Host Name")
 #   parser.add_argument("hosttyp", help="Please Enter Manager or Worker")
 #   args = parser.parse_args()

 
f = open('docker-config.yaml')
config = yaml.load(f)
f.close()
print config['master']

for worker in config['workers']
    print worker['name']
    print worker['ip']

instal()
docker_instal(master)
swarm_instal(args.hostnm, args.hosttyp)

if __name__ == "__main__":
    main()
