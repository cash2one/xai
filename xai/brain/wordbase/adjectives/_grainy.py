

#calss header
class _GRAINY():
	def __init__(self,): 
		self.name = "GRAINY"
		self.definitions = [u'If photographs are grainy, they are not clear because the many black and white or coloured dots that make up the image can be seen.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
