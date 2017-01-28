

#calss header
class _MIDWAY():
	def __init__(self,): 
		self.name = "MIDWAY"
		self.definitions = [u'half the distance between two places: ', u'in the middle of a process or period of time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
