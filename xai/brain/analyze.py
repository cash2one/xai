import os
import nltk
nltk.data.path.append("/afs/psi.ch/user/w/wang_x3/xing/apps/nltk_data")
from xai1.brain.memory import Memory

class Analyze():
    '''
    '''
    def __init__(self, ):
        self.keyword = None
        self.specie = None
        self.exit = False
        self.parents = []
        self.childen = []

        self.memory = Memory()
        pass

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
                    # print(defition)
                    # self.parents, self.childen= self.sent_analyze(defition)
                    # print(self.parents, self.childen)
                    # classdata = 
                    self.sent_analyze(defition)
                    print(self.relation_analyze)
                    classdata = self.relation_analyze(defition)

        return classdata

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
            relation_analyze = self.relation_adj
        elif 'adv' in specie:
            specie = 'adverbs'
            relation_analyze = self.relation_adv
        elif 'pre' in specie:
            specie = 'prepositions'
            relation_analyze = self.relation_pre
        elif 'suffix' in specie:
            specie = 'conjunctions'
            relation_analyze = self.relation_suffix
        elif 'pro' in specie:
            specie = 'pronouns'
            relation_analyze = self.relation_pro
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
    def sent_analyze(self, defition):
        '''
        find conjunctions: and, or
        find preposition: with
        '''
        result = ""
        # print(defition)
        sent = nltk.word_tokenize(defition)
        conj = self.find_conjunctions(sent)
        prep = self.find_prepositions(sent)
        print(conj)
        print(prep)

        return sent
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
    def relation_adj(self, defition):
        pass
    #
    def relation_adv(self, defition):
        pass
    #
    def relation_pre(self, defition):
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
    def relation_pro(self, defition):
        pass
    #
    def relation_suffix(self, defition):
        pass
    #

# Run main function by default
if __name__ == "__main__":
    myanalyze = Analyze()