

#calss header
class _MONOCHROME():
	def __init__(self,): 
		self.name = "MONOCHROME"
		self.definitions = [u'using only black, white, and grey, or using only one colour: ', u'not interesting or exciting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
