from Commands.update import Update

# pip install gitpython
import git
import os

class UpdateCheck(Update):

    def configure(self):
        self.name = "update:check";
        self.description = "check for updates";

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
        # tagList=repo.git.ls_remote("--tags", "orgin")
        print(tags[-1])
        # print(tagList[-1])

        return int(count) > 0