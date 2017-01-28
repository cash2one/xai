

#calss header
class _FULFILLING():
	def __init__(self,): 
		self.name = "FULFILLING"
		self.definitions = [u'making you feel happy and satisfied: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
