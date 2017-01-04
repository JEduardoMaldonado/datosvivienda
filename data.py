import json

class data:  
    data = []

    def read(self):
        with open('data/vivienda.json','r') as file:
            data = json.load(file)
            self.data = data['results'] 

   
