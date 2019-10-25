import contentful
from pygit2 import Repository

branch_name = Repository('.').head.shorthand

client = contentful.Client('vv5raolukrc9', 
                           'R_uqYKE6N7u-VzAi0bGiZaE0F7CD1n-t_uN9vwvRYOU',
                           environment=branch_name)

entry = client.entry('15jwOBqpxqSAOy2eOO4S0m')

print entry.name
