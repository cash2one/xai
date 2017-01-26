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
    #
    def update(self, filename=None, jsondata=None):
        '''
        '''
        if filename:
            self.filename = filename
        if jsondata:
            self.jsondata = jsondata

        with open(self.filename, 'r') as file:
            self.lines = file.readlines()
        file.close()

        if 'properties' in self.jsondata.keys():
            self.add_data()
    #
    def add_data(self, ):
        '''
        '''
        func_body = self.get_function('__init__')
        # print(self.filename)
        # print(func_body)
        func_body.append('''
\t\tself.properties.append('{0}')
'''.format(self.jsondata['properties']))
        # print(func_body)
        self.remove_function('__init__')
        self.lines += func_body
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
        # print(self.functions)
        index = self.functions['name'].index(funcname)
        
        if index==(len(self.functions['index']) - 1):
            end = -1
        else:
            # print(index, len(self.functions['index']))
            end = self.functions['index'][index+1]
        func_body = self.lines[self.functions['index'][index]:end]
        return func_body
    #
    def remove_function(self, funcname):
        '''
        '''
        index = self.functions['name'].index(funcname)
        if index==(len(self.functions['index']) - 1):
            end = -1
        else:
            end = self.functions['index'][index+1]
        del self.lines[self.functions['index'][index]:end]
    #
    def summary_function(self, lines=None):
        '''
        '''
        if lines:
            self.lines = lines
        functions = {}
        index = []
        funcname = []
        for i, line in enumerate(self.lines):
            if 'def' in line[0:7]:
                text = re.split('def', line)
                text = re.split('\(', text[1])
                funcname.append(text[0].replace(' ',''))
                index.append(i)
        functions['index'] = index
        functions['name'] = funcname
        # print(functions)
        self.functions = functions

    def clear(self, ):
        '''
        clear old function
        '''
        pass

    
# Run main function by default
if __name__ == "__main__":
    myupdate = Update_class()
    myupdate.add_data()