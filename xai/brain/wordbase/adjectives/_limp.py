

#calss header
class _LIMP():
	def __init__(self,): 
		self.name = "LIMP"
		self.definitions = [u'soft and neither firm nor stiff: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
