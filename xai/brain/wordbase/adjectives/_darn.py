

#calss header
class _DARN():
	def __init__(self,): 
		self.name = "DARN"
		self.definitions = [u'used to emphasize what you are saying: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
