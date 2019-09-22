import serial_stuff
import save_to_txt
import time
tid_stop = 7

feather_data = serial_stuff.receive_data_from_Arduino()
while 1:
    feather_data.update()
    if (feather_data.new_data == True):
        filename = time.strftime('%Y%m%d-%H%M%S') 
        save_to_txt.create_file(filename)
        tid = time.time()

        while 1:
            feather_data.update()
            if (feather_data.new_data == True):
                feather_data.data_interpreted = True
                feather_data.new_data = False
                string = feather_data.string_received
                print(string)
                save_to_txt.save_to_txt(string+'\n', filename)
                tid = time.time()
            elif ((time.time()-tid)>tid_stop):
                print('LAger ny fil')
                break













