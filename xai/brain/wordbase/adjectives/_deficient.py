

#calss header
class _DEFICIENT():
	def __init__(self,): 
		self.name = "DEFICIENT"
		self.definitions = [u'not having enough of: ', u'not good enough: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
