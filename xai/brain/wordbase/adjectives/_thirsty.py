

#calss header
class _THIRSTY():
	def __init__(self,): 
		self.name = "THIRSTY"
		self.definitions = [u'needing to drink: ', u'Someone who is thirsty for power, knowledge, etc. wants to have it very much.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
