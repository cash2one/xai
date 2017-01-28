

#calss header
class _TANGY():
	def __init__(self,): 
		self.name = "TANGY"
		self.definitions = [u'A tangy flavour is pleasantly strong and sharp: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
