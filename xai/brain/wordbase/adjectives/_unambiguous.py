

#calss header
class _UNAMBIGUOUS():
	def __init__(self,): 
		self.name = "UNAMBIGUOUS"
		self.definitions = [u'expressed in a way that makes it completely clear what is meant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
