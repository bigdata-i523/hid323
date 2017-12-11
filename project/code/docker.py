# coding=utf-8
import subprocess
import sys
import threading
import os
import argparse

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


def docker_instal(hostnm):
    cmd = 'ssh ' + hostnm ' curl -sSL https://get.docker.com | sh'
    callproc(cmd)


def swarm_instal(hostnm, hosttyp):
    if hosttyp == "Master":
        swrmcmd = 'ssh ' + hostnm + " sudo docker swarm init "
        callproc(swrmcmd)
    else:
        joincmd = 'sudo docker swarm join-token worker'
        jointkn = callproc(joincmd)
        testsh = 'ssh ' + hostnm + ' ' + callproc(jointkn)
        callproc(testsh)

def pull():
    nodes = callproc("docker node ls | grep Ready | awk -F'[[:space:]][[:space:]]+' '{print $2}'").rstrip().split('\n')

def instal():
    step1 = callproc("sudo apt-get update -y")
    step2 = callproc("sudo apt-get -y install curl")
    step3 = callproc("sudo apt-get upgrade -y")
    step4 = callproc("sudo apt-get dist-upgrade -y")
    step5 = callproc("sudo apt-get -y install raspberrypi-ui-mods")

def main(hostnm1, master):
    parser = argparse.ArgumentParser()
    parser.add_argument("hostnm", help="Enter the Host Name")
    parser.add_argument("hosttyp", help="Please Enter Manager or Worker")
    args = parser.parse_args()

    instal()
    docker_instal(args.hostnm)
    swarm_instal(args.hostnm, args.hosttyp)


if __name__ == "__main__":
    main()
