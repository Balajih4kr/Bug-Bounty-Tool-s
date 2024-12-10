def file_open(f_name):
    with open(f_name,"r") as file:
        result = file.readlines()
        for urls in result:
            print(urls)

