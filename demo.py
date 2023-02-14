import config
from boxsdk import OAuth2, Client
from datetime import datetime

ID = config.ID[0] #set up a new app in box developer tools
key = config.key
access_token = config.access_token

auth = OAuth2(
    client_id=ID,
    client_secret=key,
    access_token= access_token
)
client = Client(auth)

user = client.user().get()
print(f'The current user ID is {user.id}')

file_id = 1140401938746
destination_path = '.'
local_file_path = 'timesheet.txt'

box_parent_folder = 194524166549
content = client.file(file_id).content()
with open(local_file_path, "a+") as file_obj:
    file_obj.write('\n')
    file_obj.write(str(datetime.now()))

updated_file = client.file(file_id).update_contents(local_file_path)
print(f'File "{updated_file.name}" has been updated')