#! /usr/bin/env python
import nltk
import textwrap
import utilities
import os
from xai.python.file import File

nltk.data.path.append("/afs/psi.ch/user/w/wang_x3/xing/apps/nltk_data")


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
        print(properties, parents)  

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
                file.write("from xai1.memory.nouns." + word + " import " + word + "\n")
                class_body += "\t\t{0}.__init__(self)\n".format(word)
                class_body += "\t\tself.parents.append(\"{0}\") \n".format(word)
            for word in  properties:
                file.write("from xai1.memory.adjectives." + word + " import " + word + "\n")
                class_body += "\t\tself.properties.append(\"{0}\") \n ".format(word)    
    

            file.write(class_body)  

        # for word in parents:
        #     class_creation(word)  

    #===============================================================================
    def read(text, grammar):
        """"""
        result = ""
        print(text)
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
            filename = self.file.pwd + '/xai1/brain/wordbase/{0}/{0}.dat'.format(specie)
            with open(filename) as file:
                print(filename)
                self.wordbase[specie] = json.load(file)
            file.close()
    #
    def save_wordbase(self,):
        '''
        '''
        import json
        for specie in self.wordbase:
            filename = self.file.pwd + '/xai1/brain/wordbase/{0}/{0}.dat'.format(specie)
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
        pass
    def build_class(self,):
        '''
        '''
        class_body = '''\n
#calss header
class _{0}():
\tdef __init__(self): 
\t\tself.name = "{0}" \n'''.format(self.word)
    #
        filename = self.file.pwd + '/xai1/brain/wordbase/{0}/_{1}.py'.format(self.specie, self.word)
        with open(filename, 'w') as file:
            file.write(class_body)
        new_class = {}
        new_class[self.word] = '_{0}'.format(self.word)
        self.wordbase[self.specie].update(new_class)
    #
    def check_specie(self, specie):
        '''
        '''
        if 'verb' in specie:
            self.specie = 'verbs'
            self.builder = self.builder_verb
        elif 'noun' in specie:
            self.specie = 'nouns'
            self.builder = self.builder_noun
        elif 'adj' in specie:
            self.specie = 'adjectives'
            self.builder = self.builder_adj
        elif 'adv' in specie:
            self.specie = 'adverbs'
            self.builder = self.builder_adv
        elif 'pre' in specie:
            self.specie = 'prepositions'
            self.builder = self.builder_pre
        elif 'suffix' in specie or 'conj' in specie:
            self.specie = 'conjunctions'
            self.builder = self.builder_con
        elif 'pro' in specie:
            self.specie = 'pronouns'
            self.builder = self.builder_pro
        elif 'num' in specie:
            self.specie = 'numbers'
            self.builder = self.builder_num
        else:
            print('>>>>>> {0} specie "{1}" error'.format(self.word, specie))
    #
    def builder_verb(self,):
        '''
        '''
        # self.build_class()
        self.build_class()

        pass
    #
    def builder_noun(self,):
        '''
        '''
        self.build_class()
        pass
    #
    def builder_pre(self,):
        '''
        '''
        self.build_class()

        pass
    #
    def builder_adj(self,):
        '''
        '''
        self.build_class()

        pass
    #
    def builder_adv(self,):
        '''
        '''
        pass
    #
    def builder_con(self,):
        '''
        '''
        self.build_class()

        pass
    #
    def builder_num(self,):
        '''
        '''
        self.build_class()

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
    from xai1.body.eye import Eye
    from xai1.python.file import File
    eye = Eye()
    file = File()
    mymemory = Memory()
    filename = file.pwd + '/xai1/examples/word/wordbase.dat'
    jsonword = eye.read_json(filename)
    # print(jsonword)
    mymemory.word.build_word(jsonword)