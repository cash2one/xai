

#calss header
class _TEEMING():
	def __init__(self,): 
		self.name = "TEEMING"
		self.definitions = [u'If a place is teeming, it is full of people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
