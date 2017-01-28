

#calss header
class _INNOVATIVE():
	def __init__(self,): 
		self.name = "INNOVATIVE"
		self.definitions = [u'using new methods or ideas: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
