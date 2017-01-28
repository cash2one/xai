

#calss header
class _ARTY():
	def __init__(self,): 
		self.name = "ARTY"
		self.definitions = [u'being or wishing to seem very interested in everything connected with art and artists: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
