

#calss header
class _SEAGOING():
	def __init__(self,): 
		self.name = "SEAGOING"
		self.definitions = [u'(of ships) built for travelling across the sea, not just near the coast and on rivers']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
