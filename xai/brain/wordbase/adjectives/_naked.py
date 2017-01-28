

#calss header
class _NAKED():
	def __init__(self,): 
		self.name = "NAKED"
		self.definitions = [u'not covered by clothes: ', u'Something that is naked does not have its usual covering: ', u'A naked feeling or quality is not hidden, although it is bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
