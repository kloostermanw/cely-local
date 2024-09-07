from Commands.command import Command

# pip install gitpython
import git
import os

class Module(Command):

    def configure(self):
        self.name = "main:update";
        self.description = "update command";

    def handle(self, args):
        self.check()

        
    def update(self):
        repo = self.getRepo()
        o = repo.remotes.origin
        o.pull("--rebase")

    def check(self):
        repo = self.getRepo()
        commits = list(repo.iter_commits('HEAD'))
        count = len(commits)
        print(count)

    def getRepo(self):
        blnVerbose = False
        sourceBranch = 'develop'

        if (os.path.exists(".git") == False):
            print(".git not found.")
            exit(0)

        repo = git.Repo(search_parent_directories=True)
        branch = repo.active_branch

        if branch.name == sourceBranch:
            if blnVerbose:
                print(branch.name)
        else:
            print('no ' + sourceBranch + ' branch found' +  ' but ' + branch.name)
            exit(0)

        if repo.untracked_files:
            print(sourceBranch + ' branch has untracked files')
            exit(0)

        # if repo.is_dirty():
        #     print(sourceBranch + ' branch has uncommitted files')
        #     exit(0)
        
        return repo