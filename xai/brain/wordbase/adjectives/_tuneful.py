

#calss header
class _TUNEFUL():
	def __init__(self,): 
		self.name = "TUNEFUL"
		self.definitions = [u'with a pleasant tune: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
