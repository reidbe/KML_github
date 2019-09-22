import serial_stuff
import save_to_txt
import time
tid_stop = 7

feather_data = serial_stuff.receive_data_from_Arduino()
coordinates = []
print("Starter opp lagring av kordinater")
while 1:
    feather_data.update()
    if (feather_data.new_data == True):
        print("starter på ny fil")
        filename = time.strftime("%Y%m%d-%H%M%S")  # Create file name, on this form 'yyyymmdd-hhmmss'
        save_to_txt.create_file(filename)
        tid = time.perf_counter()

        while 1:
            feather_data.update()
            if (feather_data.new_data == True):
                feather_data.data_interpreted = True
                feather_data.new_data = False
                string = feather_data.string_received[:feather_data.string_received.index("\r")]
                print(string)
                save_to_txt.save_to_txt(string+'\n', filename)
                tid = time.perf_counter()
            elif ((time.perf_counter()-tid)>tid_stop):
                #Avbryter, tatt for lang tid fra forrige målepunkt mottatt
                print("avbryter lagring")
                break













