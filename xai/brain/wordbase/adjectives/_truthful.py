

#calss header
class _TRUTHFUL():
	def __init__(self,): 
		self.name = "TRUTHFUL"
		self.definitions = [u'honest and not containing or telling any lies: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
