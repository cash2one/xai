

#calss header
class _STATELESS():
	def __init__(self,): 
		self.name = "STATELESS"
		self.definitions = [u'A stateless person has no country that they officially belong to.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
