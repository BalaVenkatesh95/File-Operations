'''
Take name of text file , read and display content into console
'''
#def - keyword to define a function
#r - to open file in read mode
def read_file(filename):
    file = open(filename, "r")
    file_details = file.read()
    print(file_details)
#if __name__ == '__main__': interpreter jumps directly into this line and executes based on provided
if __name__ == '__main__':
    file_name = "timestampnow.txt"
    read_file(file_name)
