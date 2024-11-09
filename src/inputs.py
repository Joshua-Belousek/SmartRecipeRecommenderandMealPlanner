import csv
import json

def read_ingredients_csv(file):
    with open(file, mode = 'r') as file: #open the file on reading mode
        ingredients = []
        reader = csv.reader(file)
        next(reader) # skip the header of the file
        for row in reader:
            ingredients.append({
                "name": row[0].lower(),     
                "quantity": int(row[1]),
                "unit": row[2]})
                  
    return ingredients      #ingredients[0]['name'] will access the name of the first ingredient

#function to read Json file
def read_Json(file):
    with open(file, mode='r') as file:
        prefrences = json.load(file)
    return prefrences