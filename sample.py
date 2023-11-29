import paramiko

class SSHClient:
    def __init__(self, host, port, username, password=None, key_filename=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.key_filename = key_filename
        self.client = None

    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            if self.key_filename:
                self.client.connect(self.host, self.port, self.username, key_filename=self.key_filename)
            else:
                self.client.connect(self.host, self.port, self.username, password=self.password)
            print(f"Connected to {self.host}:{self.port}")
        except Exception as e:
            print(f"Error connecting to {self.host}:{self.port}: {str(e)}")
            raise

    def execute_command(self, command):
        if not self.client:
            print("Not connected. Call connect() method first.")
            return None

        try:
            stdin, stdout, stderr = self.client.exec_command(command)
            output = stdout.read().decode('utf-8')
            error = stderr.read().decode('utf-8')

            if error:
                print(f"Error executing command '{command}': {error}")
            else:
                print(f"Command '{command}' executed successfully.")
                return output

        except Exception as e:
            print(f"Error executing command '{command}': {str(e)}")
            return None

    def close(self):
        if self.client:
            self.client.close()
            print(f"Connection to {self.host}:{self.port} closed.")

# Example usage:
if __name__ == "__main__":
    # Replace the following with your SSH server details
    ssh_host = 'your_ssh_host'
    ssh_port = 22
    ssh_username = 'your_ssh_username'
    ssh_password = 'your_ssh_password'
    ssh_key_filename = 'path/to/your/private/key.pem'

    # Create an instance of SSHClient
    ssh_client = SSHClient(ssh_host, ssh_port, ssh_username, password=ssh_password, key_filename=ssh_key_filename)

    # Connect to the SSH server
    ssh_client.connect()

    # Execute commands
    output1 = ssh_client.execute_command('ls')
    output2 = ssh_client.execute_command('pwd')

    # Print the outputs
    print("Command 'ls' Output:")
    print(output1)

    print("Command 'pwd' Output:")
    print(output2)

    # Close the SSH connection
    ssh_client.close()
