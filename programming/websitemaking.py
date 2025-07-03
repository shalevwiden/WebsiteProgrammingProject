import os

assetspath='/Users/shalevwiden/Downloads/Projects/website_programming_project/programming/assets'

# create 10 folders called assetstorage{num} each with one markdown and one csv
# I'll then create webasserfolders 1-5 and webassetfolders 6-10
# the tricky part will be putting the generated markdown files in the right number assetstorage files
def initialize_samplewebsite_assets():
    webassetfolders1_5='/Users/shalevwiden/Downloads/Projects/website_programming_project/website/assets/webassetfolders1-5'
    webassetfolders6_10='/Users/shalevwiden/Downloads/Projects/website_programming_project/website/assets/webassetfolders6-10'

    try:
            
        os.mkdir(path=webassetfolders1_5)
        os.mkdir(path=webassetfolders6_10)
    except FileExistsError:
        print('Yeah main folders already made\n')
    try:

        # change this right here to add more data, and everything else should follow once its run again
        '''
        In the markdown_creator_folder, the files tablecreatorscript.py and csvcreatorscript.py create the md and csv files. 
        '''
        for i in range(1,11):
            innerfolderpath=f'assetstorage{i}'
            
            if i<=5:
                fullpath=f'{webassetfolders1_5}/{innerfolderpath}'
                os.mkdir(fullpath)
            else:
                fullpath=f'{webassetfolders6_10}/{innerfolderpath}'
                os.mkdir(fullpath)
    except FileExistsError:
        print('Yeah asset folders already made\n')


# remove the leading slash
htmlfolderpath=os.path.abspath('website/html_files')
assetspath=os.path.abspath('website/assets')

def generate_websitestructure(assetfolderpath,htmlpath):
    '''
    creates an html file structure in hmtlpath for the assets in assetfolderpath
    '''

    # create a webpage for each assetstoragefolder
    

    # damn both of these work lmao
    example='assetfolder1'
    # this is what Im doing down below
    getlastdigits=example.split('e')[-1]


    # tried new method with re.split()

    # Make HTML files in subsequent folders

    htmlfiledirs=[item for item in os.listdir(htmlpath) if os.path.isdir(f'{htmlpath}/{item}')]    
    # in_folder=[item for item in os.listdir(f'{htmlpath}/{folder}') if os.path.isdir(f'{htmlpath}/{folder}/{item}')]

    maindirs=[item for item in os.listdir(assetfolderpath) if os.path.isdir(f'{assetfolderpath}/{item}')]

    for folder in maindirs:


        fullhtmlpath=f'{htmlpath}/{folder}html'
        if not os.path.exists(fullhtmlpath):
            os.mkdir(fullhtmlpath)
            print(f'Made dir at {fullhtmlpath}\n')

        fullfolderpath=os.path.join(assetfolderpath,folder)
        print(f'Full folder path" \n{fullfolderpath}')

        subfolders=os.listdir(fullfolderpath) 
        subfolders=[item for item in os.listdir(fullfolderpath) if os.path.isdir(os.path.join(fullfolderpath,item))]
       
        print(f'subfolders:{subfolders}')

        subfolders=sorted(subfolders,key=lambda x:int(x.split('e')[-1]))

        
        for subfolder in subfolders:

            fullassetsubfolderpath=os.path.join(assetfolderpath,folder,subfolder)
            print(fullassetsubfolderpath)            
            
            # sorted will do alphabetically, so I get csvfile first
            csvfile, markdownfile=sorted(os.listdir(fullassetsubfolderpath))
            
            outfactor='../'*3

            csvfilepath=os.path.join(outfactor,'assets',folder,subfolder,csvfile)
            markdownfilepath=os.path.join(outfactor,'assets',folder,subfolder,markdownfile)
            # --------------------------------------------
            # HTML Making

            # get num from the foldername
            num=int(subfolder.split('e')[-1])

            full_html_subfolderpath=f'{fullhtmlpath}/{subfolder}files'
            print(full_html_subfolderpath)
            print('\n')
            if not os.path.exists(full_html_subfolderpath):
                os.mkdir(full_html_subfolderpath)

            print(f'Made dir at {full_html_subfolderpath}\n')

            # I have to give it an actual file name, not just .html
            filename=f'{subfolder}.html'
            full_html_filepath=f'{full_html_subfolderpath}/{filename}'
            with open(full_html_filepath,'w') as htmlassetfile:
                htmlassetfile.write(f'''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Asset Storage {num} Files</title>
    <link
      rel="stylesheet"
      href="../../../cssfiles/subfolder.css"
    />
  </head>
  <body>
   <div class="sitecontainer">
  <main>
    <h1>Asset Storage {num} Files</h1>
    <h3><a href="{markdownfilepath}">Markdown File {num}</a></h3>
    <h3><a href="{csvfilepath}" download>CSV File {num}</a></h3>
    </main>
    <footer>
      <p>Website Programming Project</p>
      <p>Shalev Widen 2025</p>
    </footer>
    </div>
  </body>
</html>
''')
                
            print(f'Made fullfile path at {full_html_filepath}\n')
        # first make all the small folders and their assets.
        # Then make the big folders with all the small folders linked
       
    
generate_websitestructure(assetfolderpath=assetspath, htmlpath=htmlfolderpath)



def generate_main_subfolders(htmlpath):

    '''
    Makes the html files for the links to the subfolder html files. The atual folder is already made, as  fullhtmlpath=f'{htmlpath}/{folder}html'
    It places those htmlfiles in those subfolders.
    I'm just using this python to generate the website. 

    This generated folders1-5index.html

    '''
    htmlfiledirs=[item for item in os.listdir(htmlpath) if os.path.isdir(f'{htmlpath}/{item}')]    

    for folder in htmlfiledirs:

        # first get the subfolder stuff
        fullfolderpath=os.path.join(htmlpath,folder)

        subfolders=os.listdir(fullfolderpath) 
        subfolders=[item for item in os.listdir(fullfolderpath) if os.path.isdir(os.path.join(fullfolderpath,item))]
       
        print(f'subfolders:\n{subfolders}\n')

        subfolders=sorted(subfolders,key=lambda x:int(x.replace('files','').split('e')[-1]))

        subfoldertext=''''''
        

        for subfolder in subfolders:
            num=subfolder.replace('files','').split('e')[-1]
            subfoldername_inhtml=f'Asset Folder {num} Files '

            html_link=subfolder.split(num)[0]+num+'.html'
            print(f'html link is \n{html_link}')
            fullhtmllink=os.path.join(subfolder,html_link)
            subfoldertext+=f''' 
            <li>
        <a href="{fullhtmllink}">
          <h3>{subfoldername_inhtml}</h3>
        </a>
      </li>'''

        fullhtmlpath=f'{htmlpath}/{folder}'
        filename=folder.replace('webasset','').replace('html','index')
        # this gives folders1-5index
        uifilename=filename.replace('index','').split('s')
        uifilename=uifilename[0]+'s '+uifilename[1]
        # this is what will be on the ui
        print(f'filename{filename}')
        print(f'fullhtmlpath{fullhtmlpath}')



        fullfilepath=f'{fullhtmlpath}/{filename}.html'
        with open(fullfilepath,'w') as htmlindexfile:
            htmlindexfile.write(f'''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{filename}</title>
    <link rel="stylesheet" href="../../cssfiles/subindexfolder.css" />
  </head>
 <body>
    <h1>Website Programming Project</h1>
    <h2>Links to {uifilename}</h2>
    <ul>{subfoldertext}</ul>

   
       <footer>
      <p>Website Programming Project</p>
      <p>Shalev Widen 2025</p>
    </footer>

  </body>
</html>

''')
            print(f'Made full file path at\n{fullfilepath}')

        
print('generate_main_subfolders\n')
generate_main_subfolders(htmlpath=htmlfolderpath)

def generate_main_index(htmlpath):
    pass