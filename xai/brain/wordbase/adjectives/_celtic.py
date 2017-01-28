

#calss header
class _CELTIC():
	def __init__(self,): 
		self.name = "CELTIC"
		self.definitions = [u'of an ancient European people who are related to the Irish, Scots, Welsh, and Bretons, or of their language or culture: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
