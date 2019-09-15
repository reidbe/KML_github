import os
import simplekml

def create_KML(filename, coordinates):
    # Create an instance of Kml
    kml = simplekml.Kml(open=1)

    # Create a linestring with two points (ie. a line)
    linestring = kml.newlinestring(name="A Line")
    linestring.coords = coordinates

    # Save the KML
    kml.save(filename + ".kml")
