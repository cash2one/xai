

#calss header
class _BATED():
	def __init__(self,): 
		self.name = "BATED"
		self.definitions = [u'in an anxious (= worried and nervous) or excited way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
