

#calss header
class _SPACIOUS():
	def __init__(self,): 
		self.name = "SPACIOUS"
		self.definitions = [u'large and with a lot of space: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
