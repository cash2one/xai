

#calss header
class _ARRANT():
	def __init__(self,): 
		self.name = "ARRANT"
		self.definitions = [u'used to say how bad something is: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
