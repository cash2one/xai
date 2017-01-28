

#calss header
class _WHEN():
	def __init__(self,): 
		self.name = "WHEN"
		self.definitions = [u'at what time; at the time at which: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
