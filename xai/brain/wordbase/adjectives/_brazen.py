

#calss header
class _BRAZEN():
	def __init__(self,): 
		self.name = "BRAZEN"
		self.definitions = [u'obvious, without any attempt to be hidden: ', u'made of or covered in brass (= a bright yellow metal): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
