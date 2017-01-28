

#calss header
class _ULCERATED():
	def __init__(self,): 
		self.name = "ULCERATED"
		self.definitions = [u'Ulcerated skin is covered in ulcers: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
