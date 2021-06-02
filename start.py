import os
cwd = os.getcwd()
print(cwd)
path = os.path.join(cwd +'\\venv\Scripts\\activate')
&&
print(path)
os.system(path)

