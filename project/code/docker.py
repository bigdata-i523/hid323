# coding=utf-8
import subprocess
import sys
import os
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
        jointkn = execssh(hostname,joincmd)
        execssh(jointkn)
        
def pull():
    nodes = callproc("docker node ls | grep Ready | awk -F'[[:space:]][[:space:]]+' '{print $2}'").rstrip().split('\n')

def instal():
   
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

instal()

f = open('docker-config.yaml')
config = yaml.load(f)
f.close()
print (config['master'])
docker_instal(master['name'])
swarm_instal(master['name','ip')

for worker in config['workers']
    print (worker['name'])
    print (worker['ip'])
    
    docker_instal(worker['name'])
    swarm_instal(worker['name','ip')


