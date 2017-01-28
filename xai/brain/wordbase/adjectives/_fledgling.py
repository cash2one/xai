

#calss header
class _FLEDGLING():
	def __init__(self,): 
		self.name = "FLEDGLING"
		self.definitions = [u'new and without experience: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
