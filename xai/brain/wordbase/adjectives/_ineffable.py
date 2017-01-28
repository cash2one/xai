

#calss header
class _INEFFABLE():
	def __init__(self,): 
		self.name = "INEFFABLE"
		self.definitions = [u'causing so much emotion, especially pleasure, that it cannot be described: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
