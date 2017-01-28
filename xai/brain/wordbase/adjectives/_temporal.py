

#calss header
class _TEMPORAL():
	def __init__(self,): 
		self.name = "TEMPORAL"
		self.definitions = [u'relating to practical matters or physical things, rather than spiritual ones', u'relating to the temple (= the side of the head behind the eyes) or the temporal bone of the skull beneath the temple: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
