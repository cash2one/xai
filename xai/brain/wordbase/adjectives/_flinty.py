

#calss header
class _FLINTY():
	def __init__(self,): 
		self.name = "FLINTY"
		self.definitions = [u'made of or like flint: ', u'severe and determined: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
