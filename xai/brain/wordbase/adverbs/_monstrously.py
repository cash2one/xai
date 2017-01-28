

#calss header
class _MONSTROUSLY():
	def __init__(self,): 
		self.name = "MONSTROUSLY"
		self.definitions = [u'in a very cruel way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
