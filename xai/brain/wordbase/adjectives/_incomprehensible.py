

#calss header
class _INCOMPREHENSIBLE():
	def __init__(self,): 
		self.name = "INCOMPREHENSIBLE"
		self.definitions = [u'impossible or extremely difficult to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
