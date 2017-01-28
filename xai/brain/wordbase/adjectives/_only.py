

#calss header
class _ONLY():
	def __init__(self,): 
		self.name = "ONLY"
		self.definitions = [u'used to show that there is a single one or very few of something, or that there are no others: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
