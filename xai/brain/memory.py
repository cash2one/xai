#!/usr/bin/env python
import nltk
from xai.python.file import File
from xai.python.update_class import Update_class
import os

class Memory():
    '''
    '''
    def __init__(self, ):
        '''
        '''
        self.file = File()
        self.update_class = Update_class()
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
        self.update_class = Update_class()
        self.word = None
        self.wordbase = {'adjectives':None, 
                         'adverbs':None,
                         'conjunctions':None,
                         'interjections':None,
                         'nouns':None,
                         'prepositions':None,
                         'pronouns':None,
                         'verbs':None,
                         'numbers':None,
                         'exclamations':None,
                         'basics':None,}
        self.otherform = {}
        #
        self.load_wordbase()
        pass
    #
    def load_wordbase(self,):
        '''
        '''
        import json
        for specie in self.wordbase:
            filename = self.file.pwd + '/xai/brain/wordbase/{0}/{0}.dat'.format(specie)
            if not os.path.exists(filename):
                self.wordbase[specie] = {}
            else:
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
            if specie == 'basics':
                filename = self.file.pwd + '/xai/brain/wordbase/{0}/{0}_1.dat'.format(specie)
                jsonword = json.dumps(self.otherform, indent=4, sort_keys=True, separators=(',', ': '))
                with open(filename, 'w') as file:
                    file.write(jsonword)
                file.close()
    #
    def build_word(self,jsonword):
        '''
        '''
        for word, species in jsonword.items():
            self.word = word
            # print(species)
            for specie in species:
                self.check_specie(specie)
                self.definitions = species[specie]
                # print(specie)
                # print(self.definitions)
                self.builder()
                if specie == 'basic':
                    self.otherform[self.word]  = self.definitions
        self.save_wordbase()
    #
    def build_word_basic(self, ):
        '''
        '''
        # read otherform
        import json
        specie = 'basics'
        filename = self.file.pwd + '/xai/brain/wordbase/{0}/{0}_1.dat'.format(specie)
        if not os.path.exists(filename):
            self.otherform = {}
        else:
            with open(filename) as file:
                self.otherform = json.load(file)
            file.close()
        i = 0
        for word in self.otherform:
            i += 1
            self.word = word
            wordbasic = self.otherform[word]
            species = self.find_word(wordbasic)
            for specie in species:
                self.specie = specie
                class_body = '''\n
from xai.brain.wordbase.{0}._{1} import _{2}

#calss header
class _{3}(_{2}, ):
\tdef __init__(self,): 
\t\t_{2}.__init__(self)
\t\tself.name = "{3}"
\t\tself.specie = '{0}'
\t\tself.basic = "{1}"
\t\tself.jsondata = {{}}
'''.format(specie, wordbasic, wordbasic.upper(), word.upper())
                filename = self.file.pwd + '/xai/brain/wordbase/{0}/_{1}.py'.format(self.specie, self.word)
                print(i, word, filename)
                with open(filename, 'w') as file:
                    file.write(class_body)
                new_class = {}
                new_class[self.word] = '_{0}'.format(self.word)
                self.wordbase[self.specie].update(new_class)
                #
                self.save_wordbase()

    #
    def find_word(self, word):
        '''
        '''
        species = []
        for specie in self.wordbase:
            if specie == 'basics':
                continue
            if word in self.wordbase[specie]:
                species.append(specie)
        return species
    #
    def modify_word(self, jsondata):
        '''
        '''
        for word, jsonword in jsondata.items():
            print(word)
            self.word = word
            species = self.find_word(word)
            for specie in species:
                self.specie = specie
                filename = self.file.pwd + '/xai/brain/wordbase/{0}/_{1}.py'.format(self.specie, self.word)
                # print(filename)
                self.update_class.update(filename, jsonword)
    #
    def build_class(self, class_body = ''):
        '''
        '''
        class_body = '''\n
#calss header
class _{0}():
\tdef __init__(self,): 
\t\tself.name = "{0}"
\t\tself.parents = []
\t\tself.childen = []
\t\tself.properties = []
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
        # print(self.word, specie)
        if 'verb' in specie[0:4]:
            self.specie = 'verbs'
            self.builder = self.builder_verb
        elif 'noun' in specie[0:4]:
            self.specie = 'nouns'
            self.builder = self.builder_noun
        elif 'adje' in specie[0:4]:
            self.specie = 'adjectives'
            self.builder = self.builder_adje
        elif 'adve' in specie[0:4]:
            self.specie = 'adverbs'
            self.builder = self.builder_adve
        elif 'prep' in specie[0:4]:
            self.specie = 'prepositions'
            self.builder = self.builder_prep
        elif 'suff' in specie[0:4] or 'conj' in specie[0:4]:
            self.specie = 'conjunctions'
            self.builder = self.builder_conj
        elif 'pron' in specie[0:4]:
            self.specie = 'pronouns'
            self.builder = self.builder_pron
        elif 'numb' in specie[0:4]:
            self.specie = 'numbers'
            self.builder = self.builder_numb
        elif 'basi' in specie[0:4]:
            self.specie = 'basics'
            self.builder = self.builder_basi
        elif 'excl' in specie[0:4]:
            self.specie = 'exclamations'
            self.builder = self.builder_excl
        else:
            print('>>>>>> {0} specie "{1}" error'.format(self.word, specie))
    #
    def builder_verb(self,):
        '''
        '''
        # self.build_class()
        class_body = '''
\t\tself.specie = 'verbs'


\tdef run(self, obj1 = [], obj2 = []):
\t\treturn self.jsondata
'''
        self.build_class(class_body)

        pass
    #
    def builder_noun(self,):
        '''
        '''
        class_body = '''
\t\tself.specie = 'nouns'


\tdef run(self, obj1 = [], obj2 = []):
\t\treturn self.jsondata
'''
        self.build_class(class_body)
    #
    def builder_prep(self,):
        '''
        '''
        class_body = '''
\t\tself.specie = 'prepositions'


\tdef run(self, obj1 = [], obj2 = []):
\t\treturn self.jsondata
'''
        self.build_class(class_body)
    #
    def builder_adje(self,):
        '''
        '''
        class_body = '''
\t\tself.specie = 'adjectives'


\tdef run(self, obj1, obj2):
\t\tself.jsondata[obj2] = {}
\t\tself.jsondata[obj2]['properties'] = self.name.lower()
\t\treturn self.jsondata
'''
        self.build_class(class_body)

        pass
    #
    def builder_adve(self,):
        '''
        '''
        class_body = '''
\t\tself.specie = 'adverbs'


\tdef run(self, obj1, obj2):
\t\tself.jsondata[obj2] = {}
\t\tself.jsondata[obj2]['properties'] = self.name.lower()
\t\treturn self.jsondata
'''
        self.build_class(class_body)
    #
    def builder_conj(self,):
        '''
        '''
        class_body = '''
\t\tself.specie = 'conjunctions'


\tdef run(self, obj1 = [], obj2 = []):
\t\treturn self.jsondata
'''
        self.build_class(class_body)
    #
    def builder_pron(self,):
        '''
        '''
        class_body = '''
\t\tself.specie = 'pronouns'


\tdef run(self, obj1 = [], obj2 = []):
\t\treturn self.jsondata
'''
        self.build_class(class_body)
    #
    def builder_numb(self,):
        '''
        '''
        class_body = '''
\t\tself.specie = 'numbers'


\tdef run(self, obj1 = [], obj2 = []):
\t\treturn self.jsondata
'''
        self.build_class(class_body)
    #
    def builder_basi(self,):
        '''
        '''
        # print(self.definitions)
        class_body = '''
\t\tself.basic = ['{0}']
'''.format(self.definitions)
        self.build_class(class_body)
    #
    def builder_excl(self,):
        '''
        '''
        # print(self.definitions)
        class_body = '''
\t\tself.specie = 'exclamations'


\tdef run(self, obj1 = [], obj2 = []):
\t\treturn self.jsondata
'''
        self.build_class(class_body)
    #
    def modify_class(self, jsondata):
        '''
        '''
        pass



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
    #==========================================================
    # # build word class
    filename = file.pwd + '/xai/words/jsonword/cambtionary.dat'
    jsonword = eye.read_json(filename)
    mymemory.word.build_word(jsonword)
    #==========================================================
    # build word in basic
    # mymemory.word.build_word_basic()
    #==========================================================
    # modify word
    jsondata = {'': {'properties': 'inside'}, 'fruit': {'properties': 'long'}, 'skin': {'properties': 'yellow'}, 'inside': {'properties': 'white'}, 'long': {'properties': 'a'}}
    mymemory.word.modify_word(jsondata)
