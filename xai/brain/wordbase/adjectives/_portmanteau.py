

#calss header
class _PORTMANTEAU():
	def __init__(self,): 
		self.name = "PORTMANTEAU"
		self.definitions = [u'consisting of a wide range of things that are considered as a single thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
