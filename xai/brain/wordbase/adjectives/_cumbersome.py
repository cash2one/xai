

#calss header
class _CUMBERSOME():
	def __init__(self,): 
		self.name = "CUMBERSOME"
		self.definitions = [u'awkward because of being large, heavy, or not effective: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
