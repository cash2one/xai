

#calss header
class _TESTY():
	def __init__(self,): 
		self.name = "TESTY"
		self.definitions = [u'easily annoyed and not patient: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
