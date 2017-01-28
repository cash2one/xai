

#calss header
class _CONTRIBUTORY():
	def __init__(self,): 
		self.name = "CONTRIBUTORY"
		self.definitions = [u'used to refer to something that you contribute to: ', u'helping to cause something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
