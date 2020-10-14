import paramiko
# import re
lista_hostow = open("devices.txt", "r")
# from getpass import getpass
# ip_address = ["192.168.2.1", "10.10.2.1"]
command = '/system identity print ; /ip address print ; /ip route print; /interface print'
# command = '/ip arp print'
# user = input("Input username: ")
# passw = getpass()
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for ip in lista_hostow:
    # lines = ip.rstrip('\n')
    ssh.connect(hostname=ip.rstrip('\n'), username='admin', password='*******')
    stdin, stdout, stderr = ssh.exec_command(command)
    stdout = stdout.readlines()
    # stdout=stdout.read().decode()
    print("Device " + ip, command)
    # print ((stdout))
    for line in stdout:
        # if ("/" or "GATEWAY") in line:
        #     print(line, end="")
        # elif "name:" in line:
        print(line, end="")
    print("\n")
    # print(re.findall("..:..:..:..:..:..", str(stdout)))
ssh.close()
lista_hostow.close()

# outputs = (stdout.read().decode())
# linie = stdout.readlines()
# out2 = stdout.read()

# print(outputs)


# print (stdout)
