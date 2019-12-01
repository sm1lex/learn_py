import os
import time
#first try to get simple backup programm

#asign source directories and files to be backed up

source = ['~/git']

#asign target dirctories where we copy backup files and folders

target_dir = '/home/aleksey/backup'


#Then file are backed up we must archive in zip file.
#and the name zip archive is the current date and time

zip_target = target_dir + os.sep + time.strftime('%Y%B%d%H%M') + '.zip'

#creat target directory if it is not present.
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  #make directory\

zip_command = 'zip -r {0} {1}'. format(zip_target, ' '.join(source))

#Run the backup
print('Zip command is:')
print(zip_command)
print('Running')

if os.system(zip_command) == 0:
    print('Successful backup to', zip_target)
else:
    print('BACKup Filed')
