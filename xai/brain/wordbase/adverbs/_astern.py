

#calss header
class _ASTERN():
	def __init__(self,): 
		self.name = "ASTERN"
		self.definitions = [u'behind a ship, or going backwards when in a ship']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
