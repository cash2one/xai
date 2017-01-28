

#calss header
class _IRREPLACEABLE():
	def __init__(self,): 
		self.name = "IRREPLACEABLE"
		self.definitions = [u'too special, unusual, or valuable to replace with something or someone else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
