

#calss header
class _FLUID():
	def __init__(self,): 
		self.name = "FLUID"
		self.definitions = [u'smooth and continuous: ', u'If situations, ideas, or plans are fluid, they are not fixed and are likely to change, often repeatedly and unexpectedly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
