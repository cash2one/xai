

#calss header
class _INBORN():
	def __init__(self,): 
		self.name = "INBORN"
		self.definitions = [u'used to refer to a mental or physical characteristic that someone has from birth: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
