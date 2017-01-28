

#calss header
class _BUSHY():
	def __init__(self,): 
		self.name = "BUSHY"
		self.definitions = [u'Bushy hair or fur is very thick: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
