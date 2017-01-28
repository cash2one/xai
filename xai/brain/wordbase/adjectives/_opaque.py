

#calss header
class _OPAQUE():
	def __init__(self,): 
		self.name = "OPAQUE"
		self.definitions = [u'preventing light from travelling through, and therefore not transparent or translucent: ', u'Opaque writing or speech is difficult to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
