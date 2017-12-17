# coding=utf-8
import subprocess
import sys
import os
import yaml
import click

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

@click.command()
@click.option('--filename', default='config.yaml', help='Name of the Configuration File.')

def main(filename):
    instal()
    # f = open('docker-config.yaml')
    f = open(filename)
    config = yaml.load(f)
    f.close()
    mastertext =  (config["master"])
    docker_instal(mastertext["name"])
    swarm_instal(mastertext["name"],mastertext["ip"])
                                               
    workerloop = (config["workers"])
    for x in workerloop:
        workertext = (x)
        docker_instal(workertext["name"])
        swarm_instal(workertext["name"],workertext["ip"])

if __name__ == '__main__':
   main()                           
                            
                            

