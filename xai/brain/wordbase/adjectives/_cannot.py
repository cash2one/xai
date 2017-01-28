

#calss header
class _CANNOT():
	def __init__(self,): 
		self.name = "CANNOT"
		self.definitions = [u'the negative form of the verb "can": ', u'used to say that something will certainly happen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
