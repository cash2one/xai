

#calss header
class _TRIBAL():
	def __init__(self,): 
		self.name = "TRIBAL"
		self.definitions = [u'relating to a tribe: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
