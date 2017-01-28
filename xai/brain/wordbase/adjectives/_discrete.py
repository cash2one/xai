

#calss header
class _DISCRETE():
	def __init__(self,): 
		self.name = "DISCRETE"
		self.definitions = [u'having a clear independent shape or form: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
