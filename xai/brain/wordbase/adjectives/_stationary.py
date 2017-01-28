

#calss header
class _STATIONARY():
	def __init__(self,): 
		self.name = "STATIONARY"
		self.definitions = [u'not moving, or not changing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
