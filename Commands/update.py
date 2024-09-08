from Commands.command import Command

# pip install gitpython
import git
import os

class Update(Command):

    def configure(self):
        self.name = "update:now";
        self.description = "Update this application";

    def handle(self, args):
        blnValue = self.updatesAvailable()
        if blnValue:
            print("update available.")

    def update(self):
        repo = self.getRepo()
        o = repo.remotes.origin
        o.pull("--rebase")

    def updatesAvailable(self):
        repo = self.getRepo()
        # git rev-list ${local}..${upstream} --count
        count = repo.git.rev_list('develop..origin/develop', '--count')


        tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
        print(tags[-1])



        return int(count) > 0

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