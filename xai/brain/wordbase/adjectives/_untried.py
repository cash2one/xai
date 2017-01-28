

#calss header
class _UNTRIED():
	def __init__(self,): 
		self.name = "UNTRIED"
		self.definitions = [u'not used before and therefore not proved to be effective: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
