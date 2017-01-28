

#calss header
class _WIGGLY():
	def __init__(self,): 
		self.name = "WIGGLY"
		self.definitions = [u'shaped like a line with many curves: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
