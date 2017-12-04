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
self.call("ssh $hostnm curl -sSL https://get.docker.com | sh”)

    
def swarm_instal(hostnm,hosttyp):
   	       if $hosttyp == “Master”:
         		self.call("sudo docker swarm init --advertise-addr " + $hostnm)
       	else:
          		jointkn = self.call("sudo docker swarm join-token worker”)
          		testsh = “ssh $hostnm  + self.call(jointkn)”
			self.call(testsh)

def pull(self):
   nodes = self.call("docker node ls | grep Ready | awk -F'[[:space:]][[:space:]]+' '{print $2}'").rstrip().split('\n')
