# Importer for EOS Cues

Uses OSC and UDP String Interface

Get your EOS IP address from the Settings in the EOS/Nomad Launcher.

Settings --> Network --> Local IP

Ensure at the bottom of that screen OSC and UDP String Interface are enabled

In your EOS Client:

System Settings --> Show Control --> String UDP
Set String RX Port to 2000

System Settings --> Show Control --> OSC
Set OSC RX Port to 2002



For the Show CSV File, the following columns are required:

Cue #
Name
Other Notes
Scene Name

Have the file in the same directory as the script and name it "lightcues.csv" with , as the delimiter

These four attributes will be imported.

To run:

```
pip install -r requirements.txt
python3 main.py
```