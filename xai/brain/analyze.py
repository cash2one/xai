from xai.python.file import File
import os
import nltk
nltk.data.path.append("/afs/psi.ch/user/w/wang_x3/xing/apps/nltk_data")
from xai.brain.memory import Memory


class Analyze():
    '''
    read sent,
    find class for each word
    jsondata = run each class
    analyze jsondata
    save memory
    '''
    def __init__(self, ):
        '''
        '''
        self.keyword = None
        self.specie = None
        self.exit = False
        self.parents = []
        self.childen = []
        self.sent = Sent()

        self.memory = Memory()

    def analyze_word(self, jsonword):
        '''
        '''
        # print(jsonword)
        for keyword, species in jsonword.items():
            self.keyword  = keyword
            for specie, defitions in species.items():
                self.specie, self.relation_analyze = self.check_specie(specie)
                self.exist = self.find_memory()
                for defition in defitions:
                    defition = self.keyword + ' is ' + defition
                    # print(defition)
                    self.find_class(defition)
                    self.sent_analyze(defition)
                    # print(self.relation_analyze)

                    classdata = self.relation_analyze(defition)

        return classdata
    #
    def check_specie(self, specie):
        '''
        '''
        if 'verb' in specie:
            specie = 'verbs'
            relation_analyze = self.relation_verb
        elif 'noun' in specie:
            specie = 'nouns'
            relation_analyze = self.relation_noun
        elif 'adj' in specie:
            specie = 'adjectives'
            relation_analyze = self.relation_adje
        elif 'adv' in specie:
            specie = 'adverbs'
            relation_analyze = self.relation_adve
        elif 'pre' in specie:
            specie = 'prepositions'
            relation_analyze = self.relation_prep
        elif 'suffix' in specie:
            specie = 'conjunctions'
            relation_analyze = self.relation_conj
        elif 'pro' in specie:
            specie = 'pronouns'
            relation_analyze = self.relation_pron
        else:
            print('>>>>>> error')
        #
        return specie, relation_analyze

    def find_memory(self):
        '''
        '''
        exist = True
        if not os.path.exists('database/{0}/_{1}.py'.format(self.specie, self.keyword)):
            exist = False
        return exist
    #===============================================================================
    def find_class(self, defition):
        '''
        find conjunctions: and, or
        find preposition: with
        '''
        result = ""
        # print(defition)
        sent = nltk.word_tokenize(defition)
        verbs = self.find_verbs(sent)
        conjs = self.find_conjunctions(sent)
        preps = self.find_prepositions(sent)
        print(verbs)
        print(conjs)
        print(preps)

        return verbs, conjs, preps
    #
    def run_class(self, ):
        '''
        '''
        pass
    #
    def find_verbs(self, sent):
        '''
        '''
        verb = []
        for word in sent:
            if word in self.memory.word.wordbase['verbs']:
                verb.append(word)
        return verb
    #
    def find_conjunctions(self, sent):
        '''
        '''
        conj = []
        for word in sent:
            if word in self.memory.word.wordbase['conjunctions']:
                conj.append(word)
        return conj
    #
    def find_prepositions(self, sent):
        '''
        '''
        prep = []
        for word in sent:
            if word in self.memory.word.wordbase['prepositions']:
                prep.append(word)
        return prep
        pass
    #
    def relation_noun(self, defitions):
        '''
        '''

        sent = self.sent_analyze(defitions)

        pass
    #
    def relation_verb(self, defition):
        pass
    #
    def relation_adje(self, defition):
        pass
    #
    def relation_adve(self, defition):
        pass
    #
    def relation_prep(self, defition):
        sent = self.sent_analyze(defition)
        childen = []
        parents = []
        properties = []
        grammar = "NP: {<VBZ>*<DT>?<JJ>*<NN>}"
        cp = nltk.RegexpParser(grammar)
        result = cp.parse(sent)
        print(result)
        for subtree in result.subtrees(filter=lambda t: t.label() == 'NP'):
            for word in subtree:
                print(word[0])
                if('JJ' in word[1]):
                    properties.append(word[0])
                if('NN' in word[1]):
                    parents.append(word[0])
            return properties, parents
        pass
    #
    def relation_pron(self, defition):
        '''
        '''
        pass
    #
    def relation_conj(self, defition):
        '''
        '''
        pass
    #

class Sent():
    '''
    '''
    def __init__(self, sent = ''):
        '''
        '''
        self.file = File()
        self.memory = Memory()
        self.sent = sent
        self.words = []
        self.word_class = {}
        self.word_species = {}
        pass
    #
    def analyze(self, sent):
        '''
        '''
        self.sent = sent
        self.find_class()
        self.run_class()

        pass
    #
    def find_class(self, ):
        '''
        find conjunctions: and, or
        find preposition: with
        '''
        import importlib
        result = ""
        # print(defition)
        import re
        self.words = re.split('; |, |\*|\n| ', self.sent)
        for word in self.words:
            self.word_class[word] = []
            self.word_species[word] = self.memory.word.find_word(word)
            for specie in self.word_species[word]:
                modulefine = 'xai.brain.wordbase.{0}._{1}'.format(specie, word)
                # print(modulefine)
                wordmodule = importlib.import_module(modulefine)
                wordclass = getattr(wordmodule, '_{0}'.format(word.upper()))
                # print(wordclass)
                self.word_class[word].append(wordclass)
    #
    def run_class(self, ):
        '''
        '''
        # adje
        for word in self.words:
            # print(self.word_class[word])
            index = self.words.index(word)
            obj1 = self.words[0:index]
            obj2 = self.words[index + 1:]
            for wordclass in self.word_class[word]:
                wordinstance = wordclass()
                print(wordinstance)
                if wordinstance.specie == 'adjectives':
                    jsondata = wordinstance.run(obj1, obj2)
                    # self.words
        # prep
        # for word in self.words:

    #
    def find_verbs(self, sent):
        '''
        '''
        verb = []
        for word in sent:
            if word in self.memory.word.wordbase['verbs']:
                verb.append(word)
        return verb
    #
    def find_conjunctions(self, sent):
        '''
        '''
        conj = []
        for word in sent:
            if word in self.memory.word.wordbase['conjunctions']:
                conj.append(word)
        return conj
    #
    def find_prepositions(self, sent):
        '''
        '''
        prep = []
        for word in sent:
            if word in self.memory.word.wordbase['prepositions']:
                prep.append(word)
        return prep
        pass


# Run main function by default
if __name__ == "__main__":
    from xai.body.eye import Eye
    eye = Eye()
    myanalyze = Analyze()
    file = File()
    #==================================================================
    # sent
    filename = file.pwd + '/xai/sents/test.dat'
    sents = eye.read_sent(filename)
    print(sents, '\n')
    for sent in sents:
        myanalyze.sent.analyze(sent)