

#calss header
class _CREDIBLE():
	def __init__(self,): 
		self.name = "CREDIBLE"
		self.definitions = [u'able to be believed or trusted: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
