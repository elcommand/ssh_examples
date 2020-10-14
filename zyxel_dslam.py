""" ZYXEL DSALM SSH z wykorzystaniem pakietu Paramiko """

import paramiko
import time

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.10.5.6', username='admin', password='********')

chan = ssh.invoke_shell()
chan.sendall('show mac address-table port 1-24'+"\r\n")
time.sleep(1)  # Bez zatrzymania na chwile skryptu nie wyświetla się listing wykonywanej komendy
s = chan.recv(4096)  # Kanał gdzie wpadną dane typu 'bytes'


""" Obieramy 'bytestring' z niepotrzebnych znaków. Usuwamy otwierające "b'" i zamykający "'", 
    ansi_escape '\x1b7' zaprzeszłość z lat 70's. Na koniec metodą 'split', wykorzystując
    jako separator '\r\n' budujemy tabelę gdzie elementy (stringi) to linie z outputu komendy """

lst = (str(s).replace(r"\x1b7", "").lstrip("b'").rstrip("'").split(r'\r\n'))

for x in lst:   # Iteracja po elementach tabeli wypluwa listing linia po lini na konsolę.
    print(x)

# chan.sendall('show version'+"\r\n")
# time.sleep(1)
# w = chan.recv(4096)
# c = ((str(w).replace(r"\x1b7", "").lstrip("b'").rstrip("'").split(r'\r\n')))
# for i in c:
#     print(i)

ssh.close()
