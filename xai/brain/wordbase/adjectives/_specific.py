

#calss header
class _SPECIFIC():
	def __init__(self,): 
		self.name = "SPECIFIC"
		self.definitions = [u'relating to one thing and not others; particular: ', u'clear and exact: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
