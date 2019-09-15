import pynmea2
import os
import simplekml
from github import Github

msg = pynmea2.parse("$GPGGA,184353.07,1929.045,S,02410.506,E,1,04,2.6,100.00,M,-33.9,M,,0000*6D")
msg1 = pynmea2.parse("$GPGGA,115739.00,4158.8441367,N,09147.4416929,W,4,13,0.9,255.747,M,-32.00,M,01,0000*6E")


# Create an instance of Kml
kml = simplekml.Kml(open=1)

# Create a linestring with two points (ie. a line)
linestring = kml.newlinestring(name="A Line")
linestring.coords = [(msg.longitude, msg.latitude), (msg1.longitude, msg1.latitude)]
# Save the KML
kml.save(os.path.splitext(__file__)[0] + ".kml")


#laste opp til github
file = open(os.path.splitext(__file__)[0] + ".kml","r")

g = Github("rei.berge@gmail.com", "snObbA2019")
org = g.get_organization('RB-KML-database')
repo = org.get_repo("test_filer")

forklaring_fil = "forklaring"


repo.create_file("kml_test2" + ".kml", forklaring_fil, file.read())

#oppdatere en fil
