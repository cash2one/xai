

#calss header
class _VENERABLE():
	def __init__(self,): 
		self.name = "VENERABLE"
		self.definitions = [u'deserving respect because of age, high position, or religious or historical importance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
