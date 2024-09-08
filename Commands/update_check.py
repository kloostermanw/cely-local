from Commands.update import Update

# pip install gitpython
import git

class UpdateCheck(Update):

    def configure(self):
        self.name = "update:check";
        self.description = "check for updates";

    def handle(self, args):
        blnValue = self.updatesAvailable()
        if blnValue:
            print("update available!")
        else:
            print("You are up-to-date.")
