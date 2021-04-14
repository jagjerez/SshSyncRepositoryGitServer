import os
from subprocess import call, STDOUT
from core.GitRepoManager import GitRepoManager
from dotenv import load_dotenv
from dotenv import dotenv_values

load_dotenv()
config = dotenv_values(".env")
pwdPath = config.PWD
os.chdir(pwdPath)#ejecuta cd {pwdPath}
#print(pwdPath)
arr = os.listdir(pwdPath)
numeroReintentos = 3
def ejecutarScriptSobreDirectorios(nombreDirectorios,_pwdPath,_numeroReintentos):
    numeroReintentos_ = _numeroReintentos
    classGit = GitRepoManager()
    for item in nombreDirectorios:

        path = os.path.join(_pwdPath,item)
        if os.path.isdir(path):

            os.chdir(path)
            if not outputCdComand:
                if call(["git", "branch"], stderr=STDOUT, stdout=open(os.devnull, 'w')) != 0:
                    try:
                        classGit.pullRepository(path)
                    except:
                        numeroReintentos_ = numeroReintentos_ - 1
                        if(numeroReintentos_ > 0):
                            ejecutarScriptSobreDirectorios(nombreDirectorios,_pwdPath,numeroReintentos_)
                else:
                    print(f'el directorio {path} no es un repositorio de git')
                    continue

ejecutarScriptSobreDirectorios(arr,pwdPath,numeroReintentos)