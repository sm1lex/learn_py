#version 2 with folder creating
import os
import time

source = ['~/git']
backup_folder = '/home/aleksey/backup'

#Check out has been folder creating
if not os.path.exists(backup_folder):
    os.mkdir(backup_folder)
    print("Folder is created")

name_backup_folder = backup_folder + os.sep + time.strftime('%Y%m%d')
name_backup_archive = time.strftime('%H%M')
#check creating name_backup_folder

if not os.path.exists(name_backup_folder):
    os.mkdir(name_backup_folder)
    print('name_backup_folder successful created')


comment = input('Enter some comment for your backup file --> ')
#check out has been comment enter
if len(comment) == 0:
    path_to_backup = name_backup_folder + os.sep + name_backup_archive
else:
    path_to_backup = name_backup_folder + os.sep + name_backup_archive + '_' + \
    comment.replace(' ', '_') + '.zip'

zip_command = 'zip -r {0} {1}'. format(path_to_backup, ' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running')
if os.system(zip_command) == 0:
    print('Successful backup file to', path_to_backup)
else:
    print('Backup FAILED')
