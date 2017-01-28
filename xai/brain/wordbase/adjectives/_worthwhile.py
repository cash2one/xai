

#calss header
class _WORTHWHILE():
	def __init__(self,): 
		self.name = "WORTHWHILE"
		self.definitions = [u'useful, important, or good enough to be a suitable reward for the money or time spent or the effort made: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
