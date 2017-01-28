

#calss header
class _SWARTHY():
	def __init__(self,): 
		self.name = "SWARTHY"
		self.definitions = [u'(of a person or their skin) dark: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
