import os

folder_original = '/Users/anastasia/Desktop/english'
folder_destination = '/Users/anastasia/Desktop/CleanedUp'
os.mkdir(folder_destination)

for entry in os.scandir(folder_original):

    location_original = os.path.join(folder_original, entry.name)
    location_destination = os.path.join(folder_destination, entry.name)

    if os.path.isfile(location_original):
        os.rename(location_original, location_destination) # позволяет перенести файл из одной директории в другую
