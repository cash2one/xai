

#calss header
class _SLIGHTED():
	def __init__(self,): 
		self.name = "SLIGHTED"
		self.definitions = [u'to feel insulted because someone has done or said something that shows that they think you are not important: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
