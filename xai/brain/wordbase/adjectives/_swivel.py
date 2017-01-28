

#calss header
class _SWIVEL():
	def __init__(self,): 
		self.name = "SWIVEL"
		self.definitions = [u'turning around a central point to face in another direction: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
