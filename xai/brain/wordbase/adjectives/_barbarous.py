

#calss header
class _BARBAROUS():
	def __init__(self,): 
		self.name = "BARBAROUS"
		self.definitions = [u'extremely cruel or unpleasant, or failing to reach acceptable social standards: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
