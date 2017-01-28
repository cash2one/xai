

#calss header
class _CONFOUNDED():
	def __init__(self,): 
		self.name = "CONFOUNDED"
		self.definitions = [u'used to express anger: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
