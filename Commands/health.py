from Commands.command import Command
import configparser
import git

class Health(Command):

    def configure(self):
        self.name = "local:health";
        self.description = "check the health of the current celery environment.";
        self.config = "health";

    def handle(self, args):
        config = self.getConfig();
        default = config['DEFAULT'];

        list = default.get('list').split(',');
        
        for r in list:
            dir = default.get(r);
            self.gitCheck(r, dir);

    def gitCheck(self, r, dir):
        repo = git.Repo(dir, search_parent_directories=True)
        branch = repo.active_branch

        # Fetch all remotes
        for remote in repo.remotes:
            remote.fetch()

        local='develop'
        upstream='origin/develop'

        ahead = repo.git.rev_list(upstream + '..' + local, count=True)
        behind = repo.git.rev_list(local + '..' + upstream, count=True)

        print("%3s %3s  %5s" % (ahead, behind, dir));