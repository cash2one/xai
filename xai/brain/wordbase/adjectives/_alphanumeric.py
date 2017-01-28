

#calss header
class _ALPHANUMERIC():
	def __init__(self,): 
		self.name = "ALPHANUMERIC"
		self.definitions = [u'containing or using letters of the alphabet and also numbers: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
