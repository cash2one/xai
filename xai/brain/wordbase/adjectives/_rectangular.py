

#calss header
class _RECTANGULAR():
	def __init__(self,): 
		self.name = "RECTANGULAR"
		self.definitions = [u'shaped like a rectangle']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
