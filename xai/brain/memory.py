import nltk
from xai.python.file import File

class Memory():
    '''
    '''
    def __init__(self, ):
        '''
        '''
        self.file = File()
        self.word = Word()
        self.sent = Sent()

        pass

    def save_memory(self, classdata):
        '''
        '''

        pass
    
    #
    def create_noun(keyword, definitions):
        """Parses the classes and saves them to the package directory as
        parsedclasses.py.
        """ 

        grammar = "Chunk: {<DT>?<JJ>*<NN><VB.><DT>?<JJ>*<NN>}"  

        properties, parents = read(definitions[0], grammar)
        # print(properties, parents)  

        # Put each class into its own module. This produces manu small files, but
        # this way it it easier for autocompletion to handle everything 

        class_paraents = ""
        for word in parents:
            class_paraents += word + ', '
        class_body = '''\n
    #calss header
    class {0}({1}):
    \tdef __init__(self): 
    \t\tself.name = "{0}"
    \t\tself.parents = []
    \t\tself.properties =[]\n'''.format(keyword, class_paraents)
        with open('../memory/nouns/_{}.py'.format(keyword), 'a') as file:
            for word in parents:
                file.write("from xai.memory.nouns." + word + " import " + word + "\n")
                class_body += "\t\t{0}.__init__(self)\n".format(word)
                class_body += "\t\tself.parents.append(\"{0}\") \n".format(word)
            for word in  properties:
                file.write("from xai.memory.adjectives." + word + " import " + word + "\n")
                class_body += "\t\tself.properties.append(\"{0}\") \n ".format(word)    
    

            file.write(class_body)  

        # for word in parents:
        #     class_creation(word)  

    #===============================================================================
    def read(text, grammar):
        """"""
        result = ""
        # print(text)
        sent = nltk.word_tokenize(text)
        sent = nltk.pos_tag(sent)
        cp = nltk.RegexpParser(grammar)
        result = cp.parse(sent)
        for subtree in result.subtrees(filter=lambda t: t.label() == 'Chunk'):
            properties = []
            parents = []
            grammar = "NP: {<VBZ><DT>?<JJ>*<NN>}"
            cp = nltk.RegexpParser(grammar) 

            result = cp.parse(subtree)  

            for subtree in result.subtrees(filter=lambda t: t.label() == 'NP'):
                for word in subtree:
                    print(word[0])
                    if('JJ' in word[1]):
                        properties.append(word[0])
                    if('NN' in word[1]):
                        parents.append(word[0])
            return properties, parents
        return [],[]

class Word():
    '''
    '''
    def __init__(self,):
        '''
        '''
        self.file = File()
        self.word = None
        self.wordbase = {'adjectives':None, 
                         'adverbs':None,
                         'conjunctions':None,
                         'interjections':None,
                         'nouns':None,
                         'prepositions':None,
                         'pronouns':None,
                         'verbs':None,
                         'numbers':None,}
        self.load_wordbase()
        pass
    #
    def load_wordbase(self,):
        '''
        '''
        import json
        for specie in self.wordbase:
            filename = self.file.pwd + '/xai/brain/wordbase/{0}/{0}.dat'.format(specie)
            with open(filename) as file:
                self.wordbase[specie] = json.load(file)
            file.close()
    #
    def save_wordbase(self,):
        '''
        '''
        import json
        for specie in self.wordbase:
            filename = self.file.pwd + '/xai/brain/wordbase/{0}/{0}.dat'.format(specie)
            jsonword = json.dumps(self.wordbase[specie], indent=4, sort_keys=True, separators=(',', ': '))
            with open(filename, 'w') as file:
                file.write(jsonword)
            file.close()
    #
    def build_word(self,jsonword):
        '''
        '''
        for word, species in jsonword.items():
            self.word = word
            for specie in species:
                self.check_specie(specie)
                self.builder()
        self.save_wordbase()
    #
    def modify_word(self, jsondata):
        '''
        '''
        for jsonword in jsondata:
            pass
        pass
    #
    def build_class(self, class_body = ''):
        '''
        '''
        class_body = '''\n
#calss header
class _{0}():
\tdef __init__(self,): 
\t\tself.name = "{0}"
\t\tself.jsondata = {{}}
'''.format(self.word.upper()) + class_body
    #
        filename = self.file.pwd + '/xai/brain/wordbase/{0}/_{1}.py'.format(self.specie, self.word)
        with open(filename, 'w') as file:
            file.write(class_body)
        new_class = {}
        new_class[self.word] = '_{0}'.format(self.word)
        self.wordbase[self.specie].update(new_class)
    #
    def check_specie(self, specie):
        '''
        '''
        print(self.word, specie)
        if 'verb' in specie[0:4]:
            self.specie = 'verbs'
            self.builder = self.builder_verb
        elif 'noun' in specie[0:4]:
            self.specie = 'nouns'
            self.builder = self.builder_noun
        elif 'adj' in specie[0:4]:
            self.specie = 'adjectives'
            self.builder = self.builder_adj
        elif 'adv' in specie[0:4]:
            self.specie = 'adverbs'
            print(self.word)
            self.builder = self.builder_adv
        elif 'pre' in specie[0:4]:
            self.specie = 'prepositions'
            self.builder = self.builder_pre
        elif 'suffix' in specie[0:4] or 'conj' in specie[0:4]:
            self.specie = 'conjunctions'
            self.builder = self.builder_con
        elif 'pro' in specie[0:4]:
            self.specie = 'pronouns'
            self.builder = self.builder_pro
        elif 'num' in specie[0:4]:
            self.specie = 'numbers'
            self.builder = self.builder_num
        else:
            print('>>>>>> {0} specie "{1}" error'.format(self.word, specie))
    #
    def builder_verb(self,):
        '''
        '''
        # self.build_class()
        class_body = '''
\tdef run(self,):
\t\treturn jsondata
'''
        self.build_class(class_body)

        pass
    #
    def builder_noun(self,):
        '''
        '''
        class_body = '''
\t\tself.parents = []
\t\tself.childen = []
'''
        self.build_class(class_body)
    #
    def builder_pre(self,):
        '''
        '''
        class_body = '''
\tdef run(self,):
\t\treturn jsondata
'''
        self.build_class(class_body)
    #
    def builder_adj(self,):
        '''
        '''
        class_body = '''
\tdef run(self, obj):
\t\tjsondata[obj] = {}
\t\tjsondata[obj]['properties'] = self.name.lower()
\t\treturn jsondata
'''
        self.build_class(class_body)

        pass
    #
    def builder_adv(self,):
        '''
        '''
        class_body = '''
\tdef run(self, verb):
\t\tjsondata[verb] = {}
\t\tjsondata[verb]['properties'] = self.name.lower()
\t\treturn jsondata
'''
        self.build_class(class_body)
    #
    def builder_con(self,):
        '''
        '''
        class_body = '''
\tdef run(self,):
\t\treturn jsondata
'''
        self.build_class(class_body)
    #
    def builder_pro(self,):
        '''
        '''
        class_body = '''
\tdef run(self,):
\t\treturn jsondata
'''
        self.build_class(class_body)
    #
    def builder_num(self,):
        '''
        '''
        class_body = '''
\tdef run(self,):
\t\treturn jsondata
'''
        self.build_class(class_body)



class Sent():
    '''
    '''
    def __init__(self,):
        '''
        '''
        pass

# Run main function by default
if __name__ == "__main__":
    from xai.body.eye import Eye
    from xai.python.file import File
    eye = Eye()
    file = File()
    mymemory = Memory()
    filename = file.pwd + '/xai/examples/word/wordbase.dat'
    jsonword = eye.read_json(filename)
    # print(jsonword)
    mymemory.word.build_word(jsonword)