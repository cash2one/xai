

#calss header
class _PUNK():
	def __init__(self,): 
		self.name = "PUNK"
		self.definitions = [u'of or relating to punk or punk rockers: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
