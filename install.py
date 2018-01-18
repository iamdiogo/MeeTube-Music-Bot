from sys import platform
import subprocess

if platform == "linux" or platform == "linux2": #if OS is linux
    bashCommand1 = "chmod 777 linux-dependencies-install.sh"
    bashCommand2 = "./linux-dependencies-install.sh"
    process = subprocess.Popen(bashCommand1.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    process = subprocess.Popen(bashCommand2.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
elif platform == "darwin": # OS X
    bashCommand1 = "chmod 777 linux-dependencies-install.sh"
    bashCommand2 = "./linux-dependencies-install.sh"
    process = subprocess.Popen(bashCommand1.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    process = subprocess.Popen(bashCommand2.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
# elif platform == "win32":
#     # Windows...
