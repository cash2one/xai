

#calss header
class _EDWARDIAN():
	def __init__(self,): 
		self.name = "EDWARDIAN"
		self.definitions = [u'from the period when Edward VII was king of England (1901-10): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
