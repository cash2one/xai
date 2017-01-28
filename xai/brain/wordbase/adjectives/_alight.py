

#calss header
class _ALIGHT():
	def __init__(self,): 
		self.name = "ALIGHT"
		self.definitions = [u'burning: ', u'brightly lit up: ', u'showing excitement and happiness: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
