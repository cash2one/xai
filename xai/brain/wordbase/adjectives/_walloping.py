

#calss header
class _WALLOPING():
	def __init__(self,): 
		self.name = "WALLOPING"
		self.definitions = [u'very big or great: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
