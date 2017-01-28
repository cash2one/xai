

#calss header
class _INEFFECTUAL():
	def __init__(self,): 
		self.name = "INEFFECTUAL"
		self.definitions = [u'not skilled at achieving, or not able to produce, good results: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
