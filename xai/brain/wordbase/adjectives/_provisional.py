

#calss header
class _PROVISIONAL():
	def __init__(self,): 
		self.name = "PROVISIONAL"
		self.definitions = [u'for the present time but likely to change: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
