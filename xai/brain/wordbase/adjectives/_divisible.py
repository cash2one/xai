

#calss header
class _DIVISIBLE():
	def __init__(self,): 
		self.name = "DIVISIBLE"
		self.definitions = [u'that can be divided by another number: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
