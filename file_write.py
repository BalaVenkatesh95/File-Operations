'''
Function will create a text file with content of current timestamp
'''
#import - helps to bring specific function or variable to current script
#from - helps to import only required function into script
from datetime import datetime
#def - keyword to define a function
#w  - to open file in write mode
def create_and_write_file():
    file = open("timestampnow.txt", "w")
    time_stamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    file.write(time_stamp)
#if __name__ == '__main__': interpreter jumps directly into this line and executes based on provided
if __name__ == '__main__':
    create_and_write_file()
