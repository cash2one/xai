

#calss header
class _FLOODED():
	def __init__(self,): 
		self.name = "FLOODED"
		self.definitions = [u'covered with water: ', u'containing a large amount or number of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
