

#calss header
class _FLAGGED():
	def __init__(self,): 
		self.name = "FLAGGED"
		self.definitions = [u'made of or covered in flagstones: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
