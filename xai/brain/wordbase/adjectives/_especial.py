

#calss header
class _ESPECIAL():
	def __init__(self,): 
		self.name = "ESPECIAL"
		self.definitions = [u'special']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
