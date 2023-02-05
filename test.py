import subprocess,string


print(subprocess.check_output("getmac",shell=True).decode())