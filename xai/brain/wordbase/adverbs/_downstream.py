

#calss header
class _DOWNSTREAM():
	def __init__(self,): 
		self.name = "DOWNSTREAM"
		self.definitions = [u'in the direction a river or stream is flowing: ', u'used to describe something that happens later in a process or series of events: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
