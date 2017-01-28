

#calss header
class _BLEEDING():
	def __init__(self,): 
		self.name = "BLEEDING"
		self.definitions = [u'used when you are annoyed with something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
