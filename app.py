
# Add required libraries
import os
import shutil
import winshell
from flask import Flask , render_template , request 
from datetime import datetime

# Create time and get user address
Time = datetime.today().ctime()
windows_user_name = os.path.expanduser('~')
windows_user_name = windows_user_name.replace("\\","/")


