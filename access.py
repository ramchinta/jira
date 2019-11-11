from jira import JIRA
options = {
    'server': '	https://axelaar.atlassian.net'}
user = 'mithrachinta@gmail.com'
apikey2 = 'nL5tOLsoihlfa29ExsVe3A85'
pwd= 'Axelaar@4'
jira = JIRA(basic_auth=(user,apikey2),options=options)
def create_issue():
    jira.create_issue(summary="Third Issue", description="Lakshman Chinta", issuetype={'name': 'Task'}, project='JF',
                              assignee={'name': 'lakshmanchinta'})



create_issue()
projects = jira.projects()
print(projects)

