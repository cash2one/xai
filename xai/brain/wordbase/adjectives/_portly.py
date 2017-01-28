

#calss header
class _PORTLY():
	def __init__(self,): 
		self.name = "PORTLY"
		self.definitions = [u'(especially of middle-aged or old men) fat and round: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
