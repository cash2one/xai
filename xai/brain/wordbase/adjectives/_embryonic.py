

#calss header
class _EMBRYONIC():
	def __init__(self,): 
		self.name = "EMBRYONIC"
		self.definitions = [u'relating to an embryo', u'starting to develop: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
