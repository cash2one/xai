

#calss header
class _PASSABLE():
	def __init__(self,): 
		self.name = "PASSABLE"
		self.definitions = [u'possible to travel on: ', u'satisfactory but not excellent: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
