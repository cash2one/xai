

#calss header
class _PRIVY():
	def __init__(self,): 
		self.name = "PRIVY"
		self.definitions = [u'to be told information that is not told to many people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
