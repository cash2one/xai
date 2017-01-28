

#calss header
class _COIFFED():
	def __init__(self,): 
		self.name = "COIFFED"
		self.definitions = [u'Coiffed hair is carefully arranged in an attractive style: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
