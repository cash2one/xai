

#calss header
class _COMPREHENSIBLE():
	def __init__(self,): 
		self.name = "COMPREHENSIBLE"
		self.definitions = [u'able to be understood: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
