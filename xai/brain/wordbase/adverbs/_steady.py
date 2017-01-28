

#calss header
class _STEADY():
	def __init__(self,): 
		self.name = "STEADY"
		self.definitions = [u'to have a romantic relationship with one person for a long period: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
