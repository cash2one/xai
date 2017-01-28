

#calss header
class _IMPLAUSIBLE():
	def __init__(self,): 
		self.name = "IMPLAUSIBLE"
		self.definitions = [u'difficult to believe, or unlikely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
