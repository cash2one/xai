

#calss header
class _OUTWARDS():
	def __init__(self,): 
		self.name = "OUTWARDS"
		self.definitions = [u'going or pointing away from a particular place or towards the outside: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
