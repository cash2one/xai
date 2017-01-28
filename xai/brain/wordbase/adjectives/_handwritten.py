

#calss header
class _HANDWRITTEN():
	def __init__(self,): 
		self.name = "HANDWRITTEN"
		self.definitions = [u'written using your hand rather than printed by a machine']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
