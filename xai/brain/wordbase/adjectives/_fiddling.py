

#calss header
class _FIDDLING():
	def __init__(self,): 
		self.name = "FIDDLING"
		self.definitions = [u'not important, or of no real interest: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
