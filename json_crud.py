"""Importing json """
import json

def read_json(filename):
    """Method to load json file"""
    try:
        with open(filename,'r',encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print('File not found')
        return None
    except Exception as e:
        print("an error occured due to: ",e)
        return None
    
def write_to_json(filename,data):
    """Method to write to json file"""
    try:
        with open(filename,'w',encoding='utf-8') as file:
            return json.dump(data , file ,indent=4)
    except Exception as e:
        print('An error occured due to: ',e)


def update_json(filename,index,key,value):
    """Method to update specific key value pair in json file"""
    try:
    #Reading the json file
        data = read_json(filename)
        print(data)
        # To update the value
        data[index][key] =value
        write_to_json(filename,data)

    except Exception as e:
        print('An exception occured due to :' ,e)


def add_data(filename,new_data):
    """Method to add new key value pair in json file"""
    try:
        # To add the value
        data = read_json(filename)
        data.append(new_data)

        write_to_json(filename,data)
    except Exception as e:
        print('An exception occured due to :' ,e)


def delete_data(filename):
    """Method to add new key value pair in json file"""
    try:
        delete_key =input("Enter the key to be deleted")
        data = read_json(filename)
        for obj in  data:
            if delete_key in obj:
                del obj[delete_key]
        write_to_json(filename,data)
    except Exception as e:
        print('An exception occured due to :' ,e)


def main():
    """Main method from where the execution starts"""

    filename = 'data.json'
    index =int(input('Enter the Index to update: '))
    key =input('Enter the Key to update: ')
    value =input('Enter the value to update: ')

    new_data = {'Name':'Krishna','Email':'Krishna@gmail.com'}
    add_data(filename,new_data)
    update_json(filename,index,key,value)
    delete_data(filename)

if __name__ =="__main__":
    main()
