

#calss header
class _BLOWSY():
	def __init__(self,): 
		self.name = "BLOWSY"
		self.definitions = [u'A blowsy woman is rather fat and looks untidy, often with badly fitting clothes.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
