

#calss header
class _TACIT():
	def __init__(self,): 
		self.name = "TACIT"
		self.definitions = [u'understood without being expressed directly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
