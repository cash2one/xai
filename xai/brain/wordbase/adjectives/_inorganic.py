

#calss header
class _INORGANIC():
	def __init__(self,): 
		self.name = "INORGANIC"
		self.definitions = [u'not being or consisting of living material, or (of chemical substances) containing no carbon or only small amounts of carbon: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
