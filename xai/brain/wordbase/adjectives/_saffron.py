

#calss header
class _SAFFRON():
	def __init__(self,): 
		self.name = "SAFFRON"
		self.definitions = [u'having a dark yellow colour']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
