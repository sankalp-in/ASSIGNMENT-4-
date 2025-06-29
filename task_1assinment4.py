try :
    a= input("Enter Name of a file(in .txt format): ")
    file = open( a , 'r')
    reading_file1 = file.readline()
    reading_file2 = file.readline()
    print("Reading file content :\nLine1: {}Line2:{}".format(reading_file1,reading_file2))
    file.close()
except FileNotFoundError :
    print("Error: The file '{}' was not found".format(a))