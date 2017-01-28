

#calss header
class _SLOVENIAN():
	def __init__(self,): 
		self.name = "SLOVENIAN"
		self.definitions = [u'\u2192\xa0 Slovene ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
