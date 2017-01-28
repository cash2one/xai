

#calss header
class _ACROSS():
	def __init__(self,): 
		self.name = "ACROSS"
		self.definitions = [u'from one side to the other of something with clear limits, such as an area of land, a road, or a river: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
