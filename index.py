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
classGit = GitRepoManager()
for item in arr:

    path = os.path.join(pwdPath,item)
    if os.path.isdir(path):

        os.chdir(path)
        if not outputCdComand:
            if call(["git", "branch"], stderr=STDOUT, stdout=open(os.devnull, 'w')) != 0:
                classGit.pullRepository(path)
            else:
                continue