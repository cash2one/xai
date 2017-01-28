

#calss header
class _ANECDOTAL():
	def __init__(self,): 
		self.name = "ANECDOTAL"
		self.definitions = [u'Anecdotal information is not based on facts or careful study: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
