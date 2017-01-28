

#calss header
class _OVERBOARD():
	def __init__(self,): 
		self.name = "OVERBOARD"
		self.definitions = [u'over the side of a boat or ship and into the water: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
