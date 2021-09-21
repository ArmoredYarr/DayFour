# Most APIS use JSON nowadays. It's important to know how to work with it.
import json #It's in the core libs.


stuff_dict = {
    "instruments" : [
        {
            "name": "ocarina",
            "type": "wind",
            "material": "ceramic"
        },
        {
            "name": "guitar",
            "type": "string",
            "material": "mahogany" 
        },
        {
            "name": "erhu",
            "type": "string",
            "material": "wood" 
        },
        {
            "name": "keyboard",
            "type": "electronic",
            "material": "abs" 
        }
    ]
}

def save_json_file(json_str, file_name):
    '''Save a dumped json string to a file [file_name].'''
    # Now you can write that to a file or send it as part of an HTTP response or whatever tickles your fancy.
    with open(file_name + '.json', 'w') as f:
        f.write(json_str)
        f.close()

def read_json_file(file_name):
    '''Read a file and return it's contents as a string.'''
    with open(file_name + '.json', 'r') as f:
        return f.read()
        

# You can dump dicts and lists into JSON strings.
# indent helps format the data to make it easier to read but is not really important unless you need it to be human readable.
stuff_str = json.dumps(stuff_dict, indent=2)

#Save the json to a text file
save_json_file(stuff_str, "stuff")

#Read the json from the text file and load it as a dict or list.
loaded_stuff = json.loads(read_json_file('stuff'))

print(loaded_stuff)

# To get the guitar from the loaded data you operate on it as you would any other list inside of a dict.
print(loaded_stuff['instruments'][1]) 
