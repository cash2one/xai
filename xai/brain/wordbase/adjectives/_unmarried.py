

#calss header
class _UNMARRIED():
	def __init__(self,): 
		self.name = "UNMARRIED"
		self.definitions = [u'not married: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
