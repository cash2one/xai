

#calss header
class _CONSUMMATE():
	def __init__(self,): 
		self.name = "CONSUMMATE"
		self.definitions = [u'perfect, or complete in every way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
