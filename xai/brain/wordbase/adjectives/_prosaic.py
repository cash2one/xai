

#calss header
class _PROSAIC():
	def __init__(self,): 
		self.name = "PROSAIC"
		self.definitions = [u'without interest, imagination, and excitement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
