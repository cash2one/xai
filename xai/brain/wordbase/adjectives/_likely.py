

#calss header
class _LIKELY():
	def __init__(self,): 
		self.name = "LIKELY"
		self.definitions = [u'If something is likely, it will probably happen or is expected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
