

#calss header
class _FLARED():
	def __init__(self,): 
		self.name = "FLARED"
		self.definitions = [u'becoming wider at one end: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
