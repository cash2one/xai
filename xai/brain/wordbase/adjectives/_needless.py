

#calss header
class _NEEDLESS():
	def __init__(self,): 
		self.name = "NEEDLESS"
		self.definitions = [u'completely unnecessary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
