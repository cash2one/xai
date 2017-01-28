

#calss header
class _REMAINING():
	def __init__(self,): 
		self.name = "REMAINING"
		self.definitions = [u'continuing to exist or be left after other parts or things have been used or taken away: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
