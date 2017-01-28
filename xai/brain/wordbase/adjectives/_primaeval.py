

#calss header
class _PRIMAEVAL():
	def __init__(self,): 
		self.name = "PRIMAEVAL"
		self.definitions = [u'\u2192\xa0 primeval ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
