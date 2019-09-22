import serial_stuff
import time
tid_stop = 7

def create_file(filename):
    save_measure_file = open(filename + '.txt', 'w')
    save_measure_file.close()


def save_to_txt(string, filename):
    save_measure_file = open(filename + '.txt', 'a')
    save_measure_file.write(string)
    save_measure_file.close()






feather_data = serial_stuff.receive_data_from_Arduino()
while 1:
    feather_data.update()
    if (feather_data.new_data == True):
        filename = time.strftime('%Y%m%d-%H%M%S') 
        create_file(filename)
        tid = time.time()

        while 1:
            feather_data.update()
            if (feather_data.new_data == True):
                feather_data.data_interpreted = True
                feather_data.new_data = False
                try:
                    string = feather_data.string_received[:feather_data.string_received.index('\r')]
                    print(string)
                    save_to_txt(string+'\n', filename)
                except:
                    a = 12              
                tid = time.time()
            elif ((time.time()-tid)>tid_stop):
                print('Lager ny fil')
                break













