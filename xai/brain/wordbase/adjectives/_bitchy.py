

#calss header
class _BITCHY():
	def __init__(self,): 
		self.name = "BITCHY"
		self.definitions = [u'often talking unkindly about other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
