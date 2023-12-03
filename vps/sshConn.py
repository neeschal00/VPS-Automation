from paramiko import SSHClient, AutoAddPolicy
from paramiko.config import SSH_PORT
from scp import SCPClient
import requests
from typing import Any, Sequence
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("sshLogs.log")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)



class SSHVPS:


    def __init__(self,ipadd,username,password,port=22) -> None:
        self.ipadd = ipadd
        self.username = username
        self.password = password
        self.port = port
        self.scp_client = None


    def createConnection(self):
        # need to create connection to use any else command
        self.connection = SSHClient()
        self.connection.set_missing_host_key_policy(AutoAddPolicy())
        self.connection.connect(self.ipadd,self.port,self.username,self.password)

    def secureCopy(self,local_path,recursive=False,remote_path=None):
        if not self.scp_client:
            self.scp_client = SCPClient(self.connection.get_transport()) #opening the socket channel to transfer files/ folders
        self.scp_client.put(local_path,remote_path=remote_path,recursive=recursive)      #transfer to remote host

    def secureDownload(self,remote_path,local_path,recursive=False):
        if not self.scp_client:
            self.scp_client = SCPClient(self.connection.get_transport()) #opening the socket channel to transfer files/ folders

        self.scp_client.get(remote_path=remote_path,local_path=local_path,recursive=recursive)


    def execCmd(self,cmd:str):
        try:
            stdin, stdout, stderr = self.connection.exec_command(cmd)
            output = stdout.read().decode('utf-8')
            error = stderr.read().decode('utf-8')

            logger.info("Execution sucess for cmd: " + cmd)
            return {
                "success": True,
                "output": output,
                "error": error
            }
        except Exception as e:
            logger.error("Error occured while executing cmd: " +str(e))
            return {
                "success": False,
                "error": str(e)
            }




if __name__ == "__main__":

    sh = SSHVPS("172.18.223.202","neeschal17","kells17")
    sh.createConnection() 
    print(sh.execCmd("ps aux"))



