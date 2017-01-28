

#calss header
class _TOPMOST():
	def __init__(self,): 
		self.name = "TOPMOST"
		self.definitions = [u'highest: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
