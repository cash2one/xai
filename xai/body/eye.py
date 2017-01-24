
import json

class Eye():
    '''
    '''
    def __init__(self, filename=None):
        self.filename = filename
        pass

    #
    def read_json(self, filename):
        '''
        '''
        if filename:
            self.filename = filename
        with open(self.filename) as file:
            jsondata = json.load(file)
        file.close()
        return jsondata
