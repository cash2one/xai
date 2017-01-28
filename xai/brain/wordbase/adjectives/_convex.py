

#calss header
class _CONVEX():
	def __init__(self,): 
		self.name = "CONVEX"
		self.definitions = [u'curved or swelling out: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
