

#calss header
class _BOYISH():
	def __init__(self,): 
		self.name = "BOYISH"
		self.definitions = [u'used to describe behaviour or characteristics that are like those of a boy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
