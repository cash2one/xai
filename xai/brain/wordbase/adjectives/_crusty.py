

#calss header
class _CRUSTY():
	def __init__(self,): 
		self.name = "CRUSTY"
		self.definitions = [u'having a hard outer layer: ', u'(especially of older people) complaining and easily annoyed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
