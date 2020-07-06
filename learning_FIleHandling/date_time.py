import datetime

#The following function creates empty file
def create_file():
    with open(filename.strftime("%Y-%m-%d-%H-%M")+".txt","w") as file : #give filename below in the main code
        file.write("shameel") # it will be written in the file..
        #to avoid the format error, we need to change it, go to --> strftime.org


filename =  datetime.datetime.now()
create_file()
