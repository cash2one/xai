

#calss header
class _SHARED():
	def __init__(self,): 
		self.name = "SHARED"
		self.definitions = [u'owned, divided, felt, or experienced by more than one person: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
