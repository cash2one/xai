

#calss header
class _CUTTING():
	def __init__(self,): 
		self.name = "CUTTING"
		self.definitions = [u'unkind and intending to upset someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
