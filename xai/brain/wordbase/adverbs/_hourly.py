

#calss header
class _HOURLY():
	def __init__(self,): 
		self.name = "HOURLY"
		self.definitions = [u'once every hour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
