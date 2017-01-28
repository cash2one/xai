from xai.python.file import File
import os
import re
class Update_class():
    '''
    add new data: replace the old __init__()
    add new function: replace the old function

    '''
    def __init__(self, ):
        '''
        '''
        self.file = File()
        self.filename = None
        self.jsondata = {}
        self.lines = []
        self.functions = {}
    #
    def update(self, filename=None, jsondata=None):
        '''
        '''
        if filename:
            self.filename = filename
        if jsondata:
            self.jsondata = jsondata
        # print(self.filename)
        with open(self.filename, 'r') as file:
            self.lines = file.readlines()
        file.close()
        #
        self.summary_function()
        if 'properties' in self.jsondata.keys():
            self.add_data()
    #
    def add_data(self, ):
        '''
        '''
        function = self.functions['__init__']
        function['body'].append('''
\t\tself.properties.append('{0}')
'''.format(self.jsondata['properties']))
        self.remove_function('__init__')
        self.lines += function['body']
        # self.print_class()
        with open(self.filename, 'w') as file:
            for line in self.lines:
                file.write(line)
        file.close()
    #
    def add_func(self, ):
        '''
        '''
        pass
    #
    def get_function(self, funcname, filename = None):
        '''
        get function body 
        '''
        func_body = None
        self.summary_function()
        func_body = self.functions[funcname]
        return func_body
    #
    def remove_function(self, funcname):
        '''
        '''
        index = self.functions[funcname]['index']
        del self.lines[index[0]:index[1]]
        self.summary_function()
        # self.print_function()
    #
    def summary_function(self, lines=None):
        '''
        functions{
        "__init__":{
                "body": [],
                "index": [start, end]
                },
        }
        '''
        self.functions = {}
        if lines:
            self.lines = lines
        function = {}
        nline = len(self.lines)
        i = 0
        #
        while i < nline:
            line = self.lines[i]
            if 'def' in line[0:7]:
                # print(i, line)
                index = []
                func_body = []
                index.append(i)
                #
                text = re.split('def', line)[1]
                text = re.split('\(', text)[0]
                funcname = text.replace(' ','')
                i += 1
                while 'def' not in self.lines[i][0:7] and i < nline - 1:
                    i += 1
                #
                if i==nline - 1:
                    end = None
                else:
                    end = i
                index.append(end)
                func_body = self.lines[index[0]:index[1]]
                function['body'] = func_body
                function['index'] = index
                self.functions[funcname] = function
                i -= 1
            i += 1
        #
    #
    def clear(self, ):
        '''
        clear old function
        '''
        pass
    #
    def print_class(self, ):
        '''
        '''
        for line in self.lines:
            print(line)
    #
    def print_function(self, funcname = None):
        '''
        '''
        for line in self.functions[funcname]['body']:
            print(line)

    
# Run main function by default
if __name__ == "__main__":
    myupdate = Update_class()
    # myupdate.add_data()