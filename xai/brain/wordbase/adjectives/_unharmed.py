

#calss header
class _UNHARMED():
	def __init__(self,): 
		self.name = "UNHARMED"
		self.definitions = [u'not hurt or damaged: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
