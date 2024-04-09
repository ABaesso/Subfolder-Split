import os, fnmatch, shutil
import re

def move_files_based_on_txt(folder_path, txt_file_path):
    # legge il file txt
    with open(txt_file_path, 'r') as file:
        lines = reversed(file.readlines())#-----------------QUI---------------

    # regex per trovare le estensioni delle FOTO
    
    # modificato, se non funziona ripristinare
    regex = r"\.(.{2,5})$"        # jpg|jpeg|png)$" 
    current_subfolder = None
    #per ogni riga del file di testo
    for line in lines:
        # toglie spazi dalla stringa
        line = line.strip()
        # rimuove i caratteri unicode dalla stringa
        line = line.encode("ascii", "ignore")
        line = line.decode()

        #se è una foto
        if re.search(regex,line): 
            if current_subfolder:
                file_to_move = os.path.join(folder_path, line)
                # se il percorso della foto esiste
                if os.path.exists(file_to_move):
                    #sposta foto nella sottocartella
                    shutil.move(file_to_move, current_subfolder)
                else:
                    #controllo se è già nella cartella
                    check_for_file = os.path.join(current_subfolder,line)
                    if os.path.exists(check_for_file):
                        print(f"File'{line}' already in subfolder")
                    # la foto non è nella cartella principale e nemmeno nella sottocartella
                    else:
                        print(f"File '{line}' not found in folder.") 
        else: # se è una sottocartella
            current_subfolder = os.path.join(folder_path, line)
            #se la cartella non esiste già
            if not os.path.exists(current_subfolder):
                #la creo
                os.makedirs(current_subfolder)


#funzione che cerca il nome del file txt()
def find_txt(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


file_name= ''
folder_path = os.path.dirname(os.path.realpath(__file__))
print ('Current folder: '+ folder_path)

txt_file_path = find_txt('*.txt', folder_path)[0] # prende il primo file txt trovato(se non c'è da errore)
print('.txt file path: ' + txt_file_path)
move_files_based_on_txt(folder_path, txt_file_path)


#------------------LEGGIMI------------------
# Lo script va messo nella cartella che deve
# contenere UN file.txt (il nome non è
# importante) e le foto da mettere nelle
# sottocartelle
#
# Il file di testo deve essere composto da
# righe contenenti o il nome della foto o
# il nome della sottocartella dove vanno 
# inserite le foto.
# Se il nome della sottocartella è PRIMA
# delle foto, va tolta la scritta RIVERSE e
# salvato il file prima di lanciare lo
# script, altrimenti funziona normalmente.
#
# Lo script avvisa se le foto sono già nella
# sottocartella o se non ha trovato nella 
# cartella principale la foto.
#
# Buon lavoro -Alberto

