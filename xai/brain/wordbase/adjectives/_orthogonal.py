

#calss header
class _ORTHOGONAL():
	def __init__(self,): 
		self.name = "ORTHOGONAL"
		self.definitions = [u'relating to an angle of 90 degrees, or forming an angle of 90 degrees']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
