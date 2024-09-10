
def reader_file(f_name):
    with open(f_name,"r") as file:
        result = file.readlines()
        for i in result:
            print(i)
    
        