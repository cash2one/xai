

#calss header
class _MERITORIOUS():
	def __init__(self,): 
		self.name = "MERITORIOUS"
		self.definitions = [u'deserving great praise: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
