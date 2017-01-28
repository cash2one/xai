

#calss header
class _OLDEN():
	def __init__(self,): 
		self.name = "OLDEN"
		self.definitions = [u'from a long time ago: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
