import socket
import csv
import time

from pythonosc import udp_client

createCueString = "$ Record Cue {cuenumber} \r"

UDP_IP = "192.168.1.152"
UDP_PORT = 2000
UDP_PORT_OSC = 2002

oscClient = udp_client.SimpleUDPClient(UDP_IP, UDP_PORT_OSC)
sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)
lightCuesFile = open("lightcues.csv", "r", encoding="utf-8")

lightreader = csv.reader(lightCuesFile, delimiter=',')
reader = csv.DictReader(lightCuesFile, delimiter=',')

commands = []
oscCommands = []

for row in reader:
    cmd = createCueString.format(cuenumber=row['Cue #'])
    commands.append(cmd)

    oscCmd = ("/eos/set/cue/1/{cuenumber}/label".format(cuenumber=row['Cue #']), row['Name'])
    oscCommands.append(oscCmd)

    oscCmd = ("/eos/set/cue/1/{cuenumber}/notes".format(cuenumber=row['Cue #']), row['Other Notes'])
    oscCommands.append(oscCmd)

    if row['Scene Name'] != "":
        oscCmd = ("/eos/set/cue/1/{cuenumber}/scene".format(cuenumber=row['Cue #']), row['Scene Name'])
        oscCommands.append(oscCmd)
for command in commands:
    sock.sendto(bytes(command.encode("utf-8")), (UDP_IP, UDP_PORT))

for cmd in oscCommands:
    oscClient.send_message(cmd[0], cmd[1])

