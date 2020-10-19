#This script is built to pass in the object and a key and get back the value. Run this function by running - python test.py '{"x":{"y":{"z":"a"}}}' z
import sys

class MainProcess:
    keyword_list = list()  #Intialize Empty list to match the user input keyword with objects keywords.
    
    #This Function will traverse the input objects and Match it with the Key.
    def fetch_data_recursively(self, input_data):  
        if isinstance(input_data, dict):  #Checking if Input data is instance of Dict.
            for key, value in input_data.items():
                self.keyword_list.append(key)  #Append each keyword in object into the keyword list.
                out_data = self.fetch_data_recursively(value)  #Calling same function recursively to get value of the object.
                if out_data:
                    return out_data
        else:
            return input_data

    def process(self, input_data, keyword):
        out_data = self.fetch_data_recursively(input_data)
        if keyword in self.keyword_list:   #Matching the values with objects.
            return out_data


if __name__ == '__main__':
    argv_list = sys.argv  # Reading System Arguments Object and keyword.
    if len(argv_list) != 3:  #Check all the inputs are provided (filename,object,key)
        sys.exit("Please Enter All Arguments")
    main_process = MainProcess()
    out_data = main_process.process(eval(argv_list[1]), argv_list[2]) # Calling the process function to get desired output.
    print(out_data)