# Markdown Table File 4
### The generated markdown table is below:
  
| Column 0 | Column 1 | Column 2 | Column 3 |
|:--------:|:--------:|:--------:|:--------:|
|    4     |    4     |    4     |    4     |
|    4     |    4     |    4     |    4     |
|    4     |    4     |    4     |    4     |
<br>
<br>

It has 4 rows and 4 columns. Also headings=True is the default argument when creating the table, so it has headings.<br>In addition the values are centered due to the use of ':-:'. 

Generated from the `modified_generate_md_with_table()` function.  
And the `automate_md_and_csv_creation()` function.

```python
tableobject=createmarkdowntable3(rows=num,columns=num,placeholder=num) #headings=True
modified_generate_md_with_table(tableobject=tableobject,folderpath=fullpath)
```  

## csvfile4.csv
Also in each assetstoragefolder is a csv file. While the default is also headings=True for csv files, it is false in this case.

```python
csvobject=create_csv_object(rows=num,columns=num,placeholder=num,headings=False)
generatecsv(csvobject=csvobject,folderpath=fullpath)
```  

---
Both of those code snippets are found in `automate_md_creation(folderpath)` and `automate_csv_creation(folderpath)`, respectively. 