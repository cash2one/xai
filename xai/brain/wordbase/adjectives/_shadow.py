

#calss header
class _SHADOW():
	def __init__(self,): 
		self.name = "SHADOW"
		self.definitions = [u'used in the title of important politicians in the main opposition party (= the party not in government): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
