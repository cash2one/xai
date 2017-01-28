

#calss header
class _UNPROVEN():
	def __init__(self,): 
		self.name = "UNPROVEN"
		self.definitions = [u'not having been shown to be good enough or to be able to do something: ', u'not having been shown to be true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
