

#calss header
class _INFINITE():
	def __init__(self,): 
		self.name = "INFINITE"
		self.definitions = [u'without limits; extremely large or great: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
