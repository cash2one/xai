

#calss header
class _RULING():
	def __init__(self,): 
		self.name = "RULING"
		self.definitions = [u'being in control and making all the decisions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
