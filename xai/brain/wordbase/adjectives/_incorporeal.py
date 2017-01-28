

#calss header
class _INCORPOREAL():
	def __init__(self,): 
		self.name = "INCORPOREAL"
		self.definitions = [u'not having a physical body but a spiritual form: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
