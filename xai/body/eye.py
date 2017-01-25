from xai.python.file import File
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
    #
    def read_sent(self, filename):
        '''
        '''
        if filename:
            self.filename = filename
        with open(self.filename) as file:
            sents = file.readlines()
        file.close()
        return sents

# Run main function by default
if __name__ == "__main__":
    file = File()
    eye = Eye()
    #==================================================================
    # jsondata
    filename = file.pwd + '/xai/words/jsonword/test.dat'
    jsondata = eye.read_sent(filename)
    print(jsondata)
    #==================================================================
    # sent
    filename = file.pwd + '/xai/sents/test.dat'
    sents = eye.read_sent(filename)
    print(sents)