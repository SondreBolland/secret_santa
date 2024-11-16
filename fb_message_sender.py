from fbchat import Client
from fbchat import models
from getpass import getpass
import participants_getter

### DOES NOT FUCKING WORK. CANNOT AUTHENTICATE. MAYBE BECAUSE OF PYTHON VERSION ACCORDING TO SOME GITHUB ISSUES

client_username = 'sondrebolland@hotmail.com' #Enter your Facebook associated email. The one you use as a username
client = Client(client_username, getpass())

names = participants_getter.participant_names
profile_ids = participants_getter.participant_ids

test_name = names[0]
friend = client.searchForUsers(test_name)
message = 'test'
sent = client.send(models.Message(message), friend.uid)
if sent:
    print('The message was succesfully sent')