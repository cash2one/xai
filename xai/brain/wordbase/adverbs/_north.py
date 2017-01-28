

#calss header
class _NORTH():
	def __init__(self,): 
		self.name = "NORTH"
		self.definitions = [u'towards the north: ', u'to or in the north of the country or region: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
