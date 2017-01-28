

#calss header
class _BEASTLY():
	def __init__(self,): 
		self.name = "BEASTLY"
		self.definitions = [u'unkind or unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
