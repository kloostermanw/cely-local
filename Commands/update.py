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
        

    def check(self):
        if (os.path.exists(".git") == False):
            print(".git not found.")
            exit(0)
        
        repo = git.Repo(search_parent_directories=True)
        branch = repo.active_branch
        o = repo.remotes.origin
        o.pull()

        # print(branch)