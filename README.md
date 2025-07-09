## Website Programming Project

This project uses python to automate the creation of a basic website, in sort using it to link a variety of created csvs and md files in a variety of subfolders onto the website. Such as a 50 row and column markdown table in a markdown file or a 50 row and column csv file in a csv file.
As a result, I can regenerate the entire website in seconds with the footer on the top, for example, or with diferent H1s, titles, or links.
<br>

See the website on github pages here: [websitelink]
<br>
I created a seperate repo to deploy the website, since I had to move index.html to the root and change alot of file paths.
In the wpp_site repo, the index.html file is in the root so it can be published on github pages.

I automated the creation of the markdown and csv files from a previous project, which is on my github as
`markdowntable_andcsv_creator`.
Using the code from that project, I mass generated and placed .md files with tables in them and .csv files.

I can replace any of the md files or csv files very speedily with a diferent # of columns, rows, or placeholder quickly.

On each page you can see the .md rendered view, the .md source, and download the .md.
With the .csv you can download it.

This project has 10 Asset Storage Files, which are split up and accessed by 1-5 and 6-10. Each page links to a created markdown file and csv file, of which the number of rows and columns correlates to the number of the html file.
<br>
Many such tweaks have been made to the markdown file, which updates all created markdown files through `tablecreatorscript.py` in the `markdowntable_andcsv_creator` repo.

---

This project is both scalable and brittle.
You can easily expand the number of assets generated and the number of html files detailing those assets, such as `assetstorage1.html` for example.
However its very brittle in the fact that naming conventions cant be changed. The names have to follow a format which is pretty locked.

Take this sequence of code for example:

```python
num=subfolder.replace('files','').split('e')[-1]
subfoldername_inhtml=f'Asset Folder {num} Files'

html_link=subfolder.split(num)[0]+num+'.html'
```

`num=subfolder.replace('files','').split('e')[-1]` takes the folder name like assetstorage2files, and returns 2. Its reliant on a number being next to a 2 character as files being in the string, so it can be changed to an empty space.

This project has many such references, navigating through the `assets` folder to build a website in the `html_files` folder, definitely making it less maleable.

In this project I also learned how to add title attributes to HTML elements, how to render Markdown content dynamically in html through marked.js (like this page here, which is just the rendered README.md from [GitHub]), and how to make css text a gradient through:

```css
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
```

Also added in animations and transformations into the css code, try hovering over the substack link.

[GitHub]: https://github.com/shalevwiden/WebsiteProgrammingProject/blob/main/README.md
[websitelink]: https://shalevwiden.github.io/wpp_site/
