import os
renamePath = 'C:\\Users\\jagje\\Documents\\Arduino'
os.chdir(renamePath)#ejecuta cd {renamePath}
streamCdComand = os.popen('pwd') # obtengo el directorio de trabajo
pathOriginal = streamCdComand.read()
#print(renamePath)
arr = os.listdir(renamePath)
for item in arr:
    path = os.path.join(renamePath,item)
    if os.path.isdir(path):
        streamCdComand = os.popen(f'cd {path}')
        outputCdComand = streamCdComand.read()
        if not outputCdComand:
            os.system(f'git pull ')