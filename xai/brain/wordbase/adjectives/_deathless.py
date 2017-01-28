

#calss header
class _DEATHLESS():
	def __init__(self,): 
		self.name = "DEATHLESS"
		self.definitions = [u'lasting for ever and never to be forgotten: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
