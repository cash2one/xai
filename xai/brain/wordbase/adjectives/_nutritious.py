

#calss header
class _NUTRITIOUS():
	def __init__(self,): 
		self.name = "NUTRITIOUS"
		self.definitions = [u'containing many of the substances needed for life and growth: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
