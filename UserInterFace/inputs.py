from colorama import Fore, Back, Style
from getpass import getpass
import sys, os
import colorama
from inputExceptions import Errors, cmdMessage, isEmail

# Aquire user credentials
def Sensitive():
    email = input("Enter your email : ")
    password = getpass("Enter your password : ")
    if isEmail(email) is False:
        Errors(f"{email} is not a valid email address.", "Verification Error")
        sys.exit()
    else:
        pass

    return {'email': email, 'password': password}



# Collects data from command prompt
def InputFunc():
    data = {}

    #while validateUser(data) is False:
    data = Sensitive()
    
    dirPath = input("Enter the directory Path : ")
    fileName = input("Enter the file name :")

    return {'directoryPath' : dirPath, 'fileName' : fileName, 'userInfo': data}


def VaidateData(data):
    try:
        if (os.path.isdir(data['directoryPath'])):
            if os.path.isfile(data['directoryPath'] + "\\" +  data['fileName']):
                return True
            else:
                Errors(message=f"{data['directoryPath']}\\{data['fileName']} does not  exist.", type="File Initilization Error")
                return False
        else:
            Errors(message=f"{data['directoryPath']} does not  exist.", type="File Initilization Error")
            return False
    except KeyError:
        return False

# The main input function that handels sequential execution of functions
def UserInput():
    colorama.init()
    print(colorama.Fore.LIGHTGREEN_EX) 
    inputData = InputFunc()
    while VaidateData(inputData) is False:
        Errors("Coudn't Initilize File, Please try again", "File Initialization Failed")
        inputData = InputFunc()
    print(colorama.Fore.RESET)
    return inputData

if __name__ == "__main__":
    cmdMessage("Invalid Execution", color='Red')
