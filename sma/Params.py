import json

class Params():
    def __init__(self):
        self.duration = 0



    def load(self):
        file = open('scenario.json')

        # returns JSON object as
        # a dictionary
        data = json.load(file)

        # Iterating through the json
        # list
        return data
