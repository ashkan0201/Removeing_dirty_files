
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

"""
Collection of addresses based on the user name.
Performing calculations and deletions of addresses.

 # All addresses:
    # 1,f"{windows_user_name}/Downloads" Download > group1 >>> windows 10 and 11 
    # 2,"C:/Windows/SoftwareDistribution" windows update cleanup > group6 >>> windows 10 and 11
    # 3,f"{windows_user_name}/AppData/Local/Microsoft/Windows/Explorer" thumbnail > group3 >>> windows 10 and 11
    # 4,"C:/Windows/Logs" Windows Logs > group8 >>> windows 10 and 11
    # 5,"C:/Windows/Panther/UnattendGC" Windows upgrade log > group7 >>> windows 10 and 11
    # 6,f"{windows_user_name}/AppData/Local/Temp" _ "C:/Windows/Temp" Temporary > group4 >>> windows 10 and 11
    # 7,"C:/Windows/ServiceProfiles/NetworkService/AppData/Local/Temp" _ "C:/Windows/ServiceProfiles/NetworkService/AppData/Local/Microsoft/Windows/DeliveryOptimization" Delivery Optimization > group5 >>> windows 10 and 11
    # 8,f"{windows_user_name}/AppData/Local/NVIDIA" _ f"{windows_user_name}/AppData/Local/AMD" * (Somewhat unknown) AMD or NVIDIA Caches > group9 >>> windows 10 and 11
    # 9,f"{windows_user_name}/AppData/Local/Google/Chrome/User Data/Default/Cache" * 2  google chrome cache > group10 >>> windows 10 and 11
    # 10,f"{windows_user_name}/AppData/Local/Mozilla/Firefox/Profile" * 3 Firefox caches > group11 >>> windows 10 and 11
    # 11,f"{windows_user_name}/AppData/Local/Opera Software" * 1 opera Cache > group12== >>> windows 10 and 11
"""
@app.route("/", methods = ["GET","POST"])
def finish():

    group_list_adress = []
    try:
        if request.form["group1"]:
            group_list_adress.append(f"{windows_user_name}/Downloads")
    except:
        pass
    try:
        if request.form["group3"]:
            group_list_adress.append(f"{windows_user_name}/AppData/Local/Microsoft/Windows/Explorer")
    except:
        pass
    try:
        if request.form["group4"]:
            group_list_adress.append("C:/Windows/Temp")
            group_list_adress.append(f"{windows_user_name}/AppData/Local/Temp")
    except:
        pass
    try:
        if request.form["group5"]:
            group_list_adress.append("C:/Windows/ServiceProfiles/NetworkService/AppData/Local/Temp")
            group_list_adress.append("C:/Windows/ServiceProfiles/NetworkService/AppData/Local/Microsoft/Windows/DeliveryOptimization")
    except:
        pass
    try:
        if request.form["group6"]:
            group_list_adress.append("C:/Windows/SoftwareDistribution")
    except:
        pass
    try:
        if request.form["group7"]:
            group_list_adress.append("C:/Windows/Panther/UnattendGC")
    except:
        pass
    try:
        if request.form["group8"]:
            group_list_adress.append("C:/Windows/Logs")
    except:
        pass
    try:
        if request.form["group9"]: 
            isFolder = os.path.exists(f"{windows_user_name}/AppData/Local/NVIDIA")
            if isFolder == True:
                group_list_adress.append(f"{windows_user_name}/AppData/Local/NVIDIA/GLCache")
                group_list_adress.append(f"{windows_user_name}/AppData/Local/NVIDIA/DXCache")
                group_list_adress.append("C:/ProgramData/NVIDIA")
                group_list_adress.append("C:/ProgramData/NVIDIA Corporation/NV_Cache")
            else:
                group_list_adress.append(f"{windows_user_name}/AppData/Local/AMD/DxCache")
                group_list_adress.append(f"{windows_user_name}/AppData/Local/AMD/DxcCache")
                group_list_adress.append(f"{windows_user_name}/AppData/Local/AMD/GLCache")
                group_list_adress.append(f"{windows_user_name}/AppData/Local/AMD/VKCache")
    except:
        pass
    try:
        if request.form["group10"]:
            group_list_adress.append(f"{windows_user_name}/Local/Google/Chrome/User Data/Default/Cache")
    except:
        pass
    try:
        if request.form["group11"]:
            list_of_Firefox = []
            for Folders, Sub_Folders, Files in os.walk(f"{windows_user_name}/AppData/Local/Mozilla/Firefox/Profiles"):
                for everything in Sub_Folders:
                    list_of_Firefox.append(everything)
            for everything in list_of_Firefox:
                isFolder = os.path.exists(f"{windows_user_name}/AppData/Local/Mozilla/Firefox/Profiles/{everything}/cache2")
                if isFolder == True:
                    group_list_adress.append(f"{windows_user_name}/AppData/Local/Mozilla/Firefox/Profiles/{everything}/cache2")
                    group_list_adress.append(f"{windows_user_name}/AppData/Local/Mozilla/Firefox/Profiles/{everything}/startupCache")
    except:
        pass
    try:
        if request.form["group12"]:
            group_list_adress.append(f"{windows_user_name}/AppData/Local/Opera Software")
    except:
        pass
    try:
        if request.form["group2"]:
            RecycleBin_list = list(winshell.recycle_bin())
            for everything in RecycleBin_list: 
                with open(f'{windows_user_name}/Desktop/out_put.txt', "a+")as out_put:
                    out_put.write(f"RECYCLE BIN DELETED: {everything}" + "\n")
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)        
    except:
        pass

    """
    In this section, we prepare the obtained addresses 
    for deletion and put the output in out_put.txt
    """
    for everything in group_list_adress:
        isFolder1 = os.path.exists(everything)
        if isFolder1 == True:
            with open(f'{windows_user_name}/Desktop/out_put.txt' , "a+")as out_put:
                for Folders, Sub_Folders, Files in os.walk(everything):
                    for everything in Sub_Folders:
                        try:
                            shutil.rmtree(f"{Folders}/{everything}")
                            out_put.write(f"FOLDER IS DELETED: {Folders}/{everything}\t{Time}"+"\n")
                        except:
                            out_put.write(f"ACCESS DENIED(FOLDER IS NOT DELETED): {Folders}/{everything}\t{Time}"+"\n")
                    for everything in Files:
                        try:
                            os.unlink(f"{Folders}/{everything}")
                            out_put.write(f"FILE IS DELETED: {Folders}/{everything}\t{Time}"+"\n")
                        except:
                            out_put.write(f"ACCESS DENIED(FILE IS NOT DELETED): {Folders}/{everything}\t{Time}"+"\n")
        else:
            with open(f'{windows_user_name}/Desktop/out_put.txt' , "a+")as out_put:
                out_put.write("We could not find a folder with this address in your system. Address: "+ everything + f"\t{Time}" + "\n")
        with open(f'{windows_user_name}/Desktop/out_put.txt', "r") as file:
            data = file.read()
        with open(f'{windows_user_name}/Desktop/out_put.txt' ,"w") as file:
            file.write(data)
    return render_template("project1.html")

if __name__ == "__main__":
    app.run()