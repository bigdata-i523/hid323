# coding=utf-8
import subprocess
import sys
import threading

def call(cmd, ignore_return_code=False):
   print('Running: \n' + cmd + '\n')
   ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
   returncode = ps.wait()
   stdout = ps.communicate()[0]
   if returncode != 0 and not ignore_return_code:
       print >> sys.stderr, ('Error: command "{}" failed: {}'.format(cmd, stdout))
       sys.exit(returncode)
   else:
       return stdout


def docker_instal(hostnm):
    cmd = 'ssh hostnm curl -sSL https://get.docker.com | sh'
    self.call(cmd)


def swarm_instal(hostnm, hosttyp):
    if hosttyp == "Master":
        self.call("sudo docker swarm init --advertise-addr " + hostnm)
    else:
        joincmd = 'sudo docker swarm join-token worker'
        jointkn = self.call(joincmd)
        testsh = "ssh hostnm + self.call(jointkn)"
        self.call(testsh)

def pull(self):
    nodes = self.call("docker node ls | grep Ready | awk -F'[[:space:]][[:space:]]+' '{print $2}'").rstrip().split('\n')

def instal(self):
    step1 = self.call("sudo apt-get update -y")
    step1.wait()
    step2 = self.call("sudo apt-get -y install curl")
    step2.wait()
    step3 = self.call("sudo apt-get upgrade -y")
    step3.wait()
    step4 = self.call("sudo apt-get dist-upgrade -y")
    step4.wait()
    step5 = self.call("sudo apt-get -y install raspberrypi-ui-mods")
    step5.wait()
