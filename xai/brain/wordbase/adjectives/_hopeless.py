

#calss header
class _HOPELESS():
	def __init__(self,): 
		self.name = "HOPELESS"
		self.definitions = [u'without hope: ', u'completely without skill at a particular activity: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
