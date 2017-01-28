

#calss header
class _IMAGINARY():
	def __init__(self,): 
		self.name = "IMAGINARY"
		self.definitions = [u'Something that is imaginary is created by and exists only in the mind: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
