

#calss header
class _NURSING():
	def __init__(self,): 
		self.name = "NURSING"
		self.definitions = [u'A nursing mother is a woman who is feeding her baby with her own breast milk: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
