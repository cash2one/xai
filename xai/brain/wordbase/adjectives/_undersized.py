

#calss header
class _UNDERSIZED():
	def __init__(self,): 
		self.name = "UNDERSIZED"
		self.definitions = [u'smaller than average, or smaller than the correct size: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
