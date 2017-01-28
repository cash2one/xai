

#calss header
class _GAMINE():
	def __init__(self,): 
		self.name = "GAMINE"
		self.definitions = [u'used to describe a girl or young woman who is thin, has short hair, and is attractively like a young boy in appearance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
