
class _have():
    '''
    '''
    def __init__(self): 
        '''
        '''
        self.parents = []
        self.properties =[]
    #
    def operate(self, obj):
        '''
        '''
        if obj[1].specie == 'noun':
        	mode_1()
        elif obj[1].specie == 'ajd':
        	mode_2()
        elif obj[1].specie == 'pre':
        	mode_3()
        elif obj[1].specie == '':
        	mode_4()
        pass
    #
    def mode_1(self,):
        '''
        I've heard that story before.
        '''
        add_parents([obj[0], obj[1]])
        add_childs([obj[1], obj[0]])
        pass
    #
    def mode_2(self,):
        '''
        They have a beautiful home.
        '''
        pass
    #
    def mode_3(self,):
        '''
        Emily has a very nasty cough.
        '''
        pass
    #
    def mode_4(self,):
        '''
        We had a short walk after lunch.
        '''
        pass

