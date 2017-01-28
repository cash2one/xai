

#calss header
class _COMBATIVE():
	def __init__(self,): 
		self.name = "COMBATIVE"
		self.definitions = [u'eager to fight or argue: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
