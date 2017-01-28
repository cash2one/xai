

#calss header
class _PERCHANCE():
	def __init__(self,): 
		self.name = "PERCHANCE"
		self.definitions = [u'by chance; possibly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
