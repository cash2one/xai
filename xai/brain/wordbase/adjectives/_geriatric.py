

#calss header
class _GERIATRIC():
	def __init__(self,): 
		self.name = "GERIATRIC"
		self.definitions = [u'for or relating to old people: ', u'old and weak: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
