

#calss header
class _INDETERMINATE():
	def __init__(self,): 
		self.name = "INDETERMINATE"
		self.definitions = [u'not measured, counted, or clearly known: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
