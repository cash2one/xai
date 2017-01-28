

#calss header
class _HISTORICAL():
	def __init__(self,): 
		self.name = "HISTORICAL"
		self.definitions = [u'connected with studying or representing things from the past: ', u'used to describe prices, values, etc. in the past: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
