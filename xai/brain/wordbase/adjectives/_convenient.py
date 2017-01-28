

#calss header
class _CONVENIENT():
	def __init__(self,): 
		self.name = "CONVENIENT"
		self.definitions = [u'suitable for your purposes and needs and causing the least difficulty: ', u'near or easy to get to or use: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
