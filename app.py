
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

# Create file with code
with open(f'{windows_user_name}/Desktop/out_put.txt', "w")as out_put:
    out_put.write("(((WELCOME TO THE ELIMINATIONS OUTPUT)))\n***HISTORY***\n")

app = Flask(__name__, template_folder = "template")

@app.route("/")
def index():
    return render_template("project.html")