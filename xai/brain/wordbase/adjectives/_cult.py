

#calss header
class _CULT():
	def __init__(self,): 
		self.name = "CULT"
		self.definitions = [u'liked very much by a particular group of people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
