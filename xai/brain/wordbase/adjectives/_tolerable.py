

#calss header
class _TOLERABLE():
	def __init__(self,): 
		self.name = "TOLERABLE"
		self.definitions = [u'of a quality that is acceptable, although certainly not good: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
