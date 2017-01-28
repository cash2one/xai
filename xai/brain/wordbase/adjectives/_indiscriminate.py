

#calss header
class _INDISCRIMINATE():
	def __init__(self,): 
		self.name = "INDISCRIMINATE"
		self.definitions = [u'not showing careful thought or planning, especially so that harm results: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
