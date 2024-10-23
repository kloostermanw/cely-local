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

        #  projectv2:  https://docs.github.com/en/graphql/reference/objects#projectv2
        #  - items -> https://docs.github.com/en/graphql/reference/objects#projectv2itemconnection
        #

        #  projectv2itemconnection
        #  - node -> https://docs.github.com/en/graphql/reference/objects#projectv2item

        #  projectv2item
        #  - content -> (DraftIssue, Issue, PullRequest)



        # https://gist.github.com/richkuz/e8842fce354edbd4e12dcbfa9ca40ff6
        
        # https://github.com/longhorn/longhorn/blob/c0235113894a5baa6dbcf871caa9d54f1ea5d311/.github/workflows/scan-and-notify-testing-items.py#L134
        





        # request = requests.post('https://api.github.com/graphql',
        #                         json={'query': query},
        #                         headers=self.headers)
        
        # print(request.json())

        query = """
            query getIssueDetailsOnProject {
                node (id: "PVT_kwDOAIFBsM4Aadny") {
                    ... on ProjectV2 {
                        number
                        title
                        shortDescription
                        items {
                            totalCount
                            
                            nodes {
                                type
                                databaseId
                                content {
                                    ... on Issue {
                                    id
                                    number
                                    state
                                    }
                                }
                                status: fieldValueByName( name: "Status") {
                                    ... on ProjectV2ItemFieldSingleSelectValue {
                                        status: name
                                    }
                                }

                                # sprint: fieldValueByName(name: "Sprint") {
                                #     ... on ProjectV2ItemFieldIterationValue {
                                #         title
                                #         startDate
                                #     }
                                # }

                                
                                # fieldValues(first: 10) {
                                #     nodes {
                                #         ... on ProjectV2ItemFieldIterationValue {
                                #             title
                                #             startDate
                                #             duration
                                #             field {
                                #                 ... on ProjectV2IterationField {
                                #                 name
                                #                 }
                                #             }
                                #         }
                                #     }
                                # }

                                fieldValues(first: 30) {
                                    nodes {
                                        __typename
                                        ... on ProjectV2ItemFieldDateValue {
                                            date
                                    
                                        }

                                        ... on ProjectV2ItemFieldIterationValue {
                                            title
                                            iterationId
                                            startDate
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        """
        variables = {"projectId": '94'}
        a = self.send_query(query, variables)
        print(a)
    
    def get_project_node_id(self, project_id, organization_name):
        query = 'query{organization(login: \"' + organization_name + '\") {projectV2(number: ' + project_id + '){id}}}'
        request = requests.post('https://api.github.com/graphql',
                                json={'query': query},
                                headers=self.headers)
        return request.json()['data']['organization']['projectV2']['id']
    


    def send_query(self, query, variables=None):
        payload = {"query": query, "variables": variables}
        response = requests.post('https://api.github.com/graphql', json=payload, headers=self.headers)
        response.raise_for_status()

        return response.json()