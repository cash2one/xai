

#calss header
class _PIONEERING():
	def __init__(self,): 
		self.name = "PIONEERING"
		self.definitions = [u'using ideas and methods that have never been used before: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
