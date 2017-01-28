

#calss header
class _TERRIFIED():
	def __init__(self,): 
		self.name = "TERRIFIED"
		self.definitions = [u'very frightened: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
