

#calss header
class _DUE():
	def __init__(self,): 
		self.name = "DUE"
		self.definitions = [u'in a direction that is straight towards the north, south, east, or west: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
