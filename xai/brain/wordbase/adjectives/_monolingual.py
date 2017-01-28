

#calss header
class _MONOLINGUAL():
	def __init__(self,): 
		self.name = "MONOLINGUAL"
		self.definitions = [u'speaking or using only one language: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
