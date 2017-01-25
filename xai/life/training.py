#!/usr/bin/evn python
from xai.body.eye import Eye
from xai.brain.analyze import Analyze
from xai.brain.memory import Memory
from xai.python.file import File
import os

class Training():
    '''
    '''
    def __init__(self, kind = 'word'):
        self.file = File()
        self.kind = kind
        self.eye = Eye()
        self.analyze = Analyze()
        self.memory = Memory()
    #
    def word(self, filename='word/word.dat', style='json'):
        # filename = 'words/test.dat'
        # filename = '/usr/share/dict/linux.words'
        jsondata = self.eye.read_json(filename)
        # print(jsondata)
        classdata = self.analyze.analyze_word(jsondata)
        self.memory.save_memory(classdata)
    #
    def sent(self, filename='sent/sent.dat', style='json'):
        # filename = 'words/test.dat'
        # filename = '/usr/share/dict/linux.words'
        jsondata = self.eye.read_json(filename)
        # print(jsondata)
        classdata = self.analyze.analyze_word(jsondata)
        self.memory.save_memory(classdata)

    def article(self, ):
        pass

# Run main function by default
if __name__ == "__main__":

    mytraining = Training()
    file = File()
    filename = file.pwd + '/xai/examples/word/test.dat'
    mytraining.word(filename)