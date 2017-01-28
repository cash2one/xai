

#calss header
class _INTERMEDIATE():
	def __init__(self,): 
		self.name = "INTERMEDIATE"
		self.definitions = [u'being between two other related things, levels, or points: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
