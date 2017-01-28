

#calss header
class _SUNLIT():
	def __init__(self,): 
		self.name = "SUNLIT"
		self.definitions = [u'(of a room, etc.) receiving a lot of light from the sun: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
