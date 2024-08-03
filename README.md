# value-loader
Hi, this value loader was written without using any libraries, pure Python. :)
# Requirements
- Python 3.x
# How to use
Next to your Python script put *loader.py*, now in your script import this using `import loader`.
If you want to load something use `load("value name", "file name")`, for replacing use `replace("value name", NewValue, "file name")`.
Here are example lines of how data file should look like:
`money:float=600.0
xp:integer=1000
house:boolean=yes
status:string=Happy`
