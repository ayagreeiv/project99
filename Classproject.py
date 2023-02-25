import os
import shutil
import time

_name_ = ""

def main():
    folders = ""
    delete_folders_count = 0
    delete_file_count = 0
    
    path = 'PATH_TO_DELETE'
    days = 30
    seconds = time.time() - (days * 24 * 60 * 60)

    if os.path.exists(path):

        for root_folder, folder, files in os.walk(path):

            if seconds >= get_file_or_folder_age(root_folder):

                remove_folder(root_folder)
                delete_folders_count += 1

                break
        else:
            for folder in folders:
                folder_path = os.path.join(root_folder, file)
                
                if seconds >= get_file_or_folder_age(root_folder):
                    remove_folder(folder_path)

                    remove_folder(root_folder)
                    delete_folders_count += 1
            for file in files: 

                file_path = os.path.join(root_folder, file)
                
                if seconds >= get_file_or_folder_age(file_path):
                    remove_file(file_path)

                    remove_file(path)
                    delete_folders_count += 1
            else:

                if seconds >= get_file_or_folder_age(file_path):
                    remove_file(file_path)

                    remove_file(path)
                    delete_folders_count += 1
    else: 
        print(f'"{path}"is not found') 

    print(f'Total folders deleted: {delete_folders_count}')
    print(f'Total file deleted: {delete_file_count}')
def remove_folder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed succssfully")

    else:
        print(f" Unable to delete the "+ path)

def remove_file(path):
    if not os.remove(path):
        print(f"{path} is removed succssfully")

    else:
        print(f" Unable to delete the "+path)    

def get_file_or_folder_age(path):

    ctime = os.stat(path).st_ctime

    return ctime

if _name_ == "_main_" :
    main()



                

