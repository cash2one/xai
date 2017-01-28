

#calss header
class _DETERMINED():
	def __init__(self,): 
		self.name = "DETERMINED"
		self.definitions = [u'wanting to do something very much and not allowing anyone or any difficulties to stop you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
