

#calss header
class _TOUSLED():
	def __init__(self,): 
		self.name = "TOUSLED"
		self.definitions = [u'having hair that looks untidy, as if it has been rubbed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
