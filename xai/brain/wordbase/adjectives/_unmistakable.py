

#calss header
class _UNMISTAKABLE():
	def __init__(self,): 
		self.name = "UNMISTAKABLE"
		self.definitions = [u'not likely to be confused with something else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
