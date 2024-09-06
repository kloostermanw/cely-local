from Commands.command import Command

class Module(Command):

    def configure(self):
        self.name = "local:health";
        self.description = "check the health of the current celery environment.";

    def handle(self, args):
        print('main')
