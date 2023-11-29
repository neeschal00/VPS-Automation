from paramiko import SSHClient, AutoAddPolicy
from paramiko.config import SSH_PORT
import requests
from typing import Any, Sequence
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("sshLogs")
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


    def createConnection(self):

        self.connection = SSHClient()
        self.connection.set_missing_host_key_policy(AutoAddPolicy())
        self.connection.connect(self.ipadd,self.port,self.username,self.password)
        print(self.connection)



    def execCmd(self,cmd:str):
        cmdOutput = self.connection.exec_command(cmd)
        print(type(cmdOutput))
        return cmdOutput



if __name__ == "__main__":

    sh = SSHVPS("172.18.223.202","neeschal17","kells17")
    sh.createConnection()
    print(sh.execCmd("free"))



