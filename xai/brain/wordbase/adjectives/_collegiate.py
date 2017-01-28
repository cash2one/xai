

#calss header
class _COLLEGIATE():
	def __init__(self,): 
		self.name = "COLLEGIATE"
		self.definitions = [u'of or belonging to a college or its students: ', u'formed of colleges: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
