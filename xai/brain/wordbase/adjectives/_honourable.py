

#calss header
class _HONOURABLE():
	def __init__(self,): 
		self.name = "HONOURABLE"
		self.definitions = [u'honest and fair, or deserving praise and respect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
