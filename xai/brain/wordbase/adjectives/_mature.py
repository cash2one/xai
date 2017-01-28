

#calss header
class _MATURE():
	def __init__(self,): 
		self.name = "MATURE"
		self.definitions = [u'Mature people behave like adults in a way that shows they are well developed emotionally: ', u'A mature decision is one that is made after a lot of careful thought: ', u'completely grown physically: ', u'having a flavour that is completely developed: ', u'A mature investment is ready to be paid.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
