

#calss header
class _PHONEY():
	def __init__(self,): 
		self.name = "PHONEY"
		self.definitions = [u'not sincere or not real: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
