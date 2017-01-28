

#calss header
class _UNFILLED():
	def __init__(self,): 
		self.name = "UNFILLED"
		self.definitions = [u'An unfilled job or position has no one doing or holding it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
