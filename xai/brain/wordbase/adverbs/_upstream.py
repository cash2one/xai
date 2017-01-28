

#calss header
class _UPSTREAM():
	def __init__(self,): 
		self.name = "UPSTREAM"
		self.definitions = [u'(moving) on a river or stream towards its origin: ', u'relating to an earlier stage in a process or series of events: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
