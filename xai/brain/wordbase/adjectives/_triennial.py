

#calss header
class _TRIENNIAL():
	def __init__(self,): 
		self.name = "TRIENNIAL"
		self.definitions = [u'happening every three years: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
