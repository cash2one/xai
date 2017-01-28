

#calss header
class _STAUNCH():
	def __init__(self,): 
		self.name = "STAUNCH"
		self.definitions = [u'always loyal in supporting a person, organization, or set of beliefs or opinions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
