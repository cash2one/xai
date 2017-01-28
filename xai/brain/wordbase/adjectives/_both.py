

#calss header
class _BOTH():
	def __init__(self,): 
		self.name = "BOTH"
		self.definitions = [u'(referring to) two people or things together: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
