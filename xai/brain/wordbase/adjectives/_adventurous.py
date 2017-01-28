

#calss header
class _ADVENTUROUS():
	def __init__(self,): 
		self.name = "ADVENTUROUS"
		self.definitions = [u'willing to try new or difficult things: ', u'exciting and often dangerous: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
