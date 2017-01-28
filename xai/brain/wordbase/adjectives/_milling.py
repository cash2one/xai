

#calss header
class _MILLING():
	def __init__(self,): 
		self.name = "MILLING"
		self.definitions = [u'moving around in a large group, with no particular purpose, or in no particular direction: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
