import serial_stuff
import sys
import save_to_txt
import time
sys.path.append('/usr')
import git_repo
import pynmea2
import kml_editor
filename = time.strftime("%Y%m%d-%H%M%S")  #Create file name, on this form 'yyyymmdd-hhmmss'
save_to_txt.create_file(filename)
tid_stop = 7

feather_data = serial_stuff.receive_data_from_Arduino()
coordinates = []
tid = time.perf_counter()
while 1:
    feather_data.update()
    if (feather_data.new_data == True):
        feather_data.data_interpreted = True
        feather_data.new_data = False
        string = feather_data.string_received[:feather_data.string_received.index("\r")]
        print(string)
        msg = pynmea2.parse(string)
        if(msg.latitude!=0):    # lagrer ikkje kordinater som er 0,0 til KML-filen
            coordinates.append(( str(msg.longitude) , str(msg.latitude) ) )
        save_to_txt.save_to_txt(string+'\n', filename)
        print(coordinates)
        tid = time.perf_counter()
    elif ((time.perf_counter()-tid)>tid_stop):
        break


print('Mottar ikke data fra GPS, lagrer til KML')

if len(coordinates)>1:
    kml_editor.create_KML(filename, coordinates)
    git_repo.save_file(filename + '.kml', 'KML-fil')








