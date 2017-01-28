

#calss header
class _ILLEGAL():
	def __init__(self,): 
		self.name = "ILLEGAL"
		self.definitions = [u'not allowed by law: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
