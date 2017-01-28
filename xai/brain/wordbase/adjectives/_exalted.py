

#calss header
class _EXALTED():
	def __init__(self,): 
		self.name = "EXALTED"
		self.definitions = [u'An exalted position in an organization is a very important one: ', u'extremely happy']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
