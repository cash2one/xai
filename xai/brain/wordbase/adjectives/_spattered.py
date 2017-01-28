

#calss header
class _SPATTERED():
	def __init__(self,): 
		self.name = "SPATTERED"
		self.definitions = [u'covered with small drops of a liquid: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
