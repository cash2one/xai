

#calss header
class _ENSCONCED():
	def __init__(self,): 
		self.name = "ENSCONCED"
		self.definitions = [u'positioned safely or comfortably somewhere: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
