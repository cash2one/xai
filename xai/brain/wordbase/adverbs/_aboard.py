

#calss header
class _ABOARD():
	def __init__(self,): 
		self.name = "ABOARD"
		self.definitions = [u'on or onto a ship, aircraft, bus, or train: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
