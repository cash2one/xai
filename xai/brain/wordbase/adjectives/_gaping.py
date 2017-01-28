

#calss header
class _GAPING():
	def __init__(self,): 
		self.name = "GAPING"
		self.definitions = [u'A gaping hole or other opening is very large: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
