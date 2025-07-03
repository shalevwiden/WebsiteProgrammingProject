'''
This file is for playing around and testing. 
'''

text='assetstorage1files'
print(text.split('e'))
print()

num=text.replace('files','').split('e')[-1]
print(f'text is still {text}')
html_link=text.split(num)[0]+num+'.html'
print(f'html_link: {html_link}')
