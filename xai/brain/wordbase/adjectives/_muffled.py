

#calss header
class _MUFFLED():
	def __init__(self,): 
		self.name = "MUFFLED"
		self.definitions = [u'A muffled sound is quiet or not clear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
