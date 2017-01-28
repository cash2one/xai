

#calss header
class _IRRESISTIBLE():
	def __init__(self,): 
		self.name = "IRRESISTIBLE"
		self.definitions = [u'impossible to refuse, oppose, or avoid because it is too pleasant, attractive, or strong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
