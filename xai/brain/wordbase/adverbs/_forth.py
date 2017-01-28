

#calss header
class _FORTH():
	def __init__(self,): 
		self.name = "FORTH"
		self.definitions = [u'(from a place) out or away, or (from a point in time) forward: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
