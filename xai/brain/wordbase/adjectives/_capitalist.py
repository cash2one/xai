

#calss header
class _CAPITALIST():
	def __init__(self,): 
		self.name = "CAPITALIST"
		self.definitions = [u'based on the system of capitalism: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
