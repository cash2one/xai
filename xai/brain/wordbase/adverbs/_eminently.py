

#calss header
class _EMINENTLY():
	def __init__(self,): 
		self.name = "EMINENTLY"
		self.definitions = [u'very and obviously: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
