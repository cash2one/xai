

#calss header
class _FOLDAWAY():
	def __init__(self,): 
		self.name = "FOLDAWAY"
		self.definitions = [u'able to be folded away out of sight: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
