

#calss header
class _EXIGUOUS():
	def __init__(self,): 
		self.name = "EXIGUOUS"
		self.definitions = [u'very small in size or amount: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
