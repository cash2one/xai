

#calss header
class _EXCITED():
	def __init__(self,): 
		self.name = "EXCITED"
		self.definitions = [u'feeling very happy and enthusiastic: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
