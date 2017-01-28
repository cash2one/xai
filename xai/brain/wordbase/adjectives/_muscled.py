

#calss header
class _MUSCLED():
	def __init__(self,): 
		self.name = "MUSCLED"
		self.definitions = [u'having a lot of well-developed muscles: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
