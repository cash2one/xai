

#calss header
class _STOCHASTIC():
	def __init__(self,): 
		self.name = "STOCHASTIC"
		self.definitions = [u'A stochastic process or system is connected with random probability.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
