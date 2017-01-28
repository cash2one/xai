

#calss header
class _WORMY():
	def __init__(self,): 
		self.name = "WORMY"
		self.definitions = [u'containing worms, or infected or damaged by worms: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
