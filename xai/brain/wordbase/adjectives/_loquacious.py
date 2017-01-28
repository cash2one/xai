

#calss header
class _LOQUACIOUS():
	def __init__(self,): 
		self.name = "LOQUACIOUS"
		self.definitions = [u'Someone who is loquacious talks a lot.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
