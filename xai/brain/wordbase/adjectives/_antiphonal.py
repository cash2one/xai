

#calss header
class _ANTIPHONAL():
	def __init__(self,): 
		self.name = "ANTIPHONAL"
		self.definitions = [u'sung or played by two groups in turn: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
