from Commands.command import Command
import git
import requests

class GithubProject(Command):

    def configure(self):
        self.name = "github:project"
        self.description = ""
        self.config = "github"
        self.headers = ''

    def handle(self, args):
        COLERR = "\033[0;31m"
        COLINFO = "\033[0;35m"
        COLRESET = "\033[m"

        config = self.getConfig();
        default = config['DEFAULT'];
        org = 'celery-payroll'
        token = default.get('token');

        graphqlurl = 'https://api.github.com/graphql'
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Bearer " + token,
        }
        
        # print(self.headers)
        # node_id = self.get_project_node_id('94' ,org)
        # print(node_id)

        # https://docs.github.com/en/graphql/reference/objects#projectv2item
        
        
        query = ('query'
                 '{organization(login: \"' + org + '\")'
                    '{projectV2(number: ' + '94' + '){id, items {nodes {id, content} }}}'
                '}')


        request = requests.post('https://api.github.com/graphql',
                                json={'query': query},
                                headers=self.headers)
        
        print(request.json())


    
    def get_project_node_id(self, project_id, organization_name):
        query = 'query{organization(login: \"' + organization_name + '\") {projectV2(number: ' + project_id + '){id}}}'
        request = requests.post('https://api.github.com/graphql',
                                json={'query': query},
                                headers=self.headers)
        return request.json()['data']['organization']['projectV2']['id']