

#calss header
class _COLLATERAL():
	def __init__(self,): 
		self.name = "COLLATERAL"
		self.definitions = [u'connected but less important, or of the same family although not directly related: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
