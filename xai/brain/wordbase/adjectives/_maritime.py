

#calss header
class _MARITIME():
	def __init__(self,): 
		self.name = "MARITIME"
		self.definitions = [u'connected with human activity at sea: ', u'near the sea or coast: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
