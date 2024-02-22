import subprocess
import time
import atexit
import requests

class ssh():
    def __init__(self,user,host,local_port=8000,remote_port=3000,timeout=5):
        self.process = self.create_ssh_tunnel(local_port, remote_port, user, host)              # Create the SSH connection
        atexit.register(self.close_ssh_tunnel)                                                  # Ensure the tunnel is closed when the script exits

        print("Verifying connection")
        time.sleep(3)                                                                           # Wait a safe amount of time for the connection to be established

        self.connected = self.test_connection(local_port,timeout)

    def test_connection(self,local_port,timeout):
        try:
            url = "http://127.0.0.1:" + str(local_port) + "/test"
            response = requests.get(url, timeout=timeout)  # Adjust timeout as needed
            if response.status_code == 200:
                print("Connected")
                print("*******************************")
                return True
            else:
                print(f"Received a non-success response code: {response.status_code}")
                self.close_ssh_tunnel()
                return False
        except Exception as e:
            print(f"Connection failed. {str(e)}")
            self.close_ssh_tunnel()
            return False
            
    def create_ssh_tunnel(self,local_port, remote_port, ssh_user, ssh_host):
        command = f"ssh -L {local_port}:localhost:{remote_port} {ssh_user}@{ssh_host} -N"
        try:
            # Start the SSH tunnel
            process = subprocess.Popen(command, shell=True)
            print(f"SSH tunnel established: localhost:{local_port} -> {ssh_host}:{remote_port}")
            return process
        except Exception as e:
            print(f"Failed to create SSH tunnel: {e}")
            return None

    def close_ssh_tunnel(self):
        if self.process:
            self.process.terminate()
