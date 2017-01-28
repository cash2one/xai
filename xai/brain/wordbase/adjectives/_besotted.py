

#calss header
class _BESOTTED():
	def __init__(self,): 
		self.name = "BESOTTED"
		self.definitions = [u'completely in love with someone and always thinking of them : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
