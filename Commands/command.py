class Command:
    def __init__(self):
        self.configure()
    
    def configure(self):
        self.name = "";
        self.description = "";

    def getCommand(self):
        return self.name
    
    def getDescription(self):
        return self.description
    
    def getListItem(self):
        return {
            "command": self.name,
            "description": self.description
        }
