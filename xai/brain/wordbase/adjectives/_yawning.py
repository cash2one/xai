

#calss header
class _YAWNING():
	def __init__(self,): 
		self.name = "YAWNING"
		self.definitions = [u'used to describe a difference or amount that is extremely large and difficult to reduce: ', u'A yawning space or hole is very wide: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
