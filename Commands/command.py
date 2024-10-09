import configparser
import os.path

class Command:
    def __init__(self):
        self.configure()
    
    def configure(self):
        self.name = "";
        self.description = "";
        self.config = "";

    def getCommand(self):
        return self.name
    
    def getDescription(self):
        return self.description
    
    def getListItem(self):
        return {
            "command": self.name,
            "description": self.description
        }
    
    def getConfig(self):
        config = configparser.ConfigParser();
        config.sections();
        file1 = 'config/' + self.config + '/conf.default';
        file2 = 'config/' + self.config + '/conf';

        if (os.path.isfile(file2)):
            config.read([file1, file2])
            print('exist')
        else:
            config.read(file1);
            print('not exist')
        return config;
