

#calss header
class _STORMING():
	def __init__(self,): 
		self.name = "STORMING"
		self.definitions = [u'exciting and extremely successful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
