

#calss header
class _CORRUGATED():
	def __init__(self,): 
		self.name = "CORRUGATED"
		self.definitions = [u'(especially of sheets of iron or cardboard) having parallel rows of folds that look like a series of waves when seen from the edge: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
