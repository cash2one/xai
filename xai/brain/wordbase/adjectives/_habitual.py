

#calss header
class _HABITUAL():
	def __init__(self,): 
		self.name = "HABITUAL"
		self.definitions = [u'usual or repeated: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
