from git import Repo

class GitRepoManager:

    def pullRepository(path):
        repo = Repo(path)
        o = repo.remotes.origin
        o.pull()
