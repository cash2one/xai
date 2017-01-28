

#calss header
class _WOLFISH():
	def __init__(self,): 
		self.name = "WOLFISH"
		self.definitions = [u'like a wolf: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
