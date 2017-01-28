

#calss header
class _COLOURFUL():
	def __init__(self,): 
		self.name = "COLOURFUL"
		self.definitions = [u'having bright colours or a lot of different colours: ', u'interesting and exciting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
