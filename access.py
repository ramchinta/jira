# This script shows how to use the client in anonymous mode
# against jira.atlassian.com.
from jira import JIRA
import re

# By default, the client will connect to a JIRA instance started from the Atlassian Plugin SDK
# (see https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK for details).
# Override this with the options parameter.
options = {
    'server': '	https://axelaar.atlassian.net'}
user = 'mithrachinta@gmail.com'
apikey = 'LT7IB6kDf1tVNYrUFflW38D8'
apikey2 = 'nL5tOLsoihlfa29ExsVe3A85'
pwd= 'Axelaar@4'

oauth_dict = {
    'access_token': 'foo',
    'access_token_secret': 'bar',
    'consumer_key': 'jira-oauth-consumer',
    'key_cert': 'test'
}
jira = JIRA(basic_auth=(user,apikey2),options=options)
#jira = JIRA(options)


# Get all projects viewable by anonymous users.
projects = jira.projects()
print(projects)