

#calss header
class _PIDDLING():
	def __init__(self,): 
		self.name = "PIDDLING"
		self.definitions = [u'very small or not important: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
