

#calss header
class _CYLINDRICAL():
	def __init__(self,): 
		self.name = "CYLINDRICAL"
		self.definitions = [u'having the shape of a cylinder (= hollow tube)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
