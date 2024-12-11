'''
Tracks Desktop, if new file is added then move 
Move files
Run in the background(Constantly)
System for file Organization
need to find all file types to check what file has been added

'''

#file Organization
'''
Folders for each file type category(images,Videos,audio,text,etc)
organize by date
create subfolder with dates as their name

'''  
    
import os
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

# Configure logging
logging.basicConfig(filename='desktop_cleaner.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DesktopHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            if filename != 'storage':
                i = 1
                new_name = filename
                split_name = filename.split('.')
                base_name = ".".join(split_name[:-1])
                file_extension = split_name[-1]

                src = os.path.join(folder_to_track, filename)
                new_name = os.path.join(folder_destination, filename)

                if os.path.exists(src):
                    # Create subfolder based on file extension
                    file_extension_folder = os.path.join(folder_destination, file_extension)
                    if not os.path.exists(file_extension_folder):
                        os.makedirs(file_extension_folder)
                        logging.info(f'Created subfolder for {file_extension} files.')

                    # Check if the file already exists in the subfolder
                    while os.path.isfile(os.path.join(file_extension_folder, os.path.basename(new_name))):
                        i += 1
                        new_name = os.path.join(file_extension_folder, f"{base_name}_{i}.{file_extension}")

                    # Move the file to the corresponding subfolder
                    os.rename(src, os.path.join(file_extension_folder, os.path.basename(new_name)))
                    logging.info(f'Moved file {filename} to {file_extension} folder.')
                else:
                    logging.warning(f'Source file {filename} does not exist.')

# Input source and destination directory paths
folder_to_track = input("Enter the source directory path: ")
folder_destination = input("Enter the destination directory path: ")

# Start logging
logging.info('Script started.')

event_handler = DesktopHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
    logging.info('Script stopped.')

observer.join()

    
    
    
    
    
    
    