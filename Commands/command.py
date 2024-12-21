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
        
        baseDir = os.path.dirname(os.path.realpath(__file__));
        
        file1 = baseDir + '/../config/' + self.config + '/conf.default';
        file2 = baseDir + '/../config/' + self.config + '/conf';

        if (not os.path.isfile(file1)):
            print('config does not exist ', file1)

        if (os.path.isfile(file2)):
            config.read([file1, file2])
        else:
            config.read(file1);

        return config;
