

#calss header
class _TRANSITORY():
	def __init__(self,): 
		self.name = "TRANSITORY"
		self.definitions = [u'lasting for only a short time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
