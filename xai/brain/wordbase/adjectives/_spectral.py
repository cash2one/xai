

#calss header
class _SPECTRAL():
	def __init__(self,): 
		self.name = "SPECTRAL"
		self.definitions = [u'coming from or seeming to be the spirit of a dead person: ', u'of the set of colours into which a beam of light can be separated: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
