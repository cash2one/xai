

#calss header
class _NONPAREIL():
	def __init__(self,): 
		self.name = "NONPAREIL"
		self.definitions = [u'better than any other: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
