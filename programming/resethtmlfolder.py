import os
import shutil

'''
Running this file deletes all folders in "foldersfolders"
'''
htmlfolderpath='/Users/shalevwiden/Downloads/Projects/website_programming_project/website/html_files'


def resethtmlfolder(htmlfolderpath):
    folders=os.listdir(htmlfolderpath)
    
    delcount=0
    for folder in folders:
        if '50' not in folder and os.path.isdir(folder):
            fullpath=f'{htmlfolderpath}/{folder}'
            
            try:
                # shutil.rmtree deletes folder and all contents inside it
                shutil.rmtree(fullpath)
                delcount += 1
            except PermissionError:
                print(f"Permission denied: {fullpath}\n")
            except Exception as e:
                print(f"Failed to delete {fullpath}: {e}")


    print(f'Ran resethtmlfolder.\n{delcount} folders were deleted.')

def main():
    resethtmlfolder(htmlfolderpath=htmlfolderpath)

# this will delete web asset 50 though so be careful
active =False
if active:
    if __name__=='__main__':
        main()
