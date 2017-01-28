

#calss header
class _GUTTURAL():
	def __init__(self,): 
		self.name = "GUTTURAL"
		self.definitions = [u'(of speech sounds) produced at the back of the throat and therefore deep: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
