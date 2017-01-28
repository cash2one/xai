

#calss header
class _FEBRILE():
	def __init__(self,): 
		self.name = "FEBRILE"
		self.definitions = [u'extremely active, or too excited, imaginative, or emotional: ', u'caused by a fever: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
