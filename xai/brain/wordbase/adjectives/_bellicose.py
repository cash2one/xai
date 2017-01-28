

#calss header
class _BELLICOSE():
	def __init__(self,): 
		self.name = "BELLICOSE"
		self.definitions = [u'wishing to fight or start a war: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
