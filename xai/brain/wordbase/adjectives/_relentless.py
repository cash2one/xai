

#calss header
class _RELENTLESS():
	def __init__(self,): 
		self.name = "RELENTLESS"
		self.definitions = [u'continuing in a severe or extreme way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
