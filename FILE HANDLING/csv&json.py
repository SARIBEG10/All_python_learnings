"""CREATE CSV and JSON files"""

path = "saribeg.csv"
file = open(path, "w")
file.write("Hello World!")


file_json = open("Sari.json", "w")
file_json.write('{"name" : "Saribeg",'
                '"lastname": "farmanian"}')

