#!/usr/bin/evn python
from xai.body.eye import Eye
from xai.brain.analyze import Analyze
from xai.brain.memory import Memory
import os

class Training():
    '''
    '''
    def __init__(self, kind = 'word'):
        self.kind = kind
        self.eye = Eye()
        self.analyze = Analyze()
        self.memory = Memory()
    #
    def word(self, filename='word/word.dat', style='json'):
        # filename = 'words/test.dat'
        # filename = '/usr/share/dict/linux.words'
        jsondata = self.eye.read_json(filename)
        print(jsondata)
        classdata = self.analyze.analyze_word(jsondata)
        self.memory.save_memory(classdata)

    def article(self, ):
        pass


class Learn():
    '''
    '''
    def __init__(self, kind = 'word'):
        self.kind = kind
        self.eye = Eye()
        self.analyze = Analyze()
        self.memory = Memory()
    #
    def word(self, filename='word/word.dat', style='json'):
        # filename = 'words/test.dat'
        # filename = '/usr/share/dict/linux.words'
        jsondata = self.eye.read_json(filename)
        print(jsondata)
        classdata = self.analyze.analyze_word(jsondata)
        self.memory.save_memory(classdata)

    def article(self, ):
        pass


