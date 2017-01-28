

#calss header
class _CURVY():
	def __init__(self,): 
		self.name = "CURVY"
		self.definitions = [u'containing a lot of curves: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
