

#calss header
class _SOMBRE():
	def __init__(self,): 
		self.name = "SOMBRE"
		self.definitions = [u'serious, sad, and without humour or entertainment: ', u'dark and plain: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
