

#calss header
class _THEREON():
	def __init__(self,): 
		self.name = "THEREON"
		self.definitions = [u'on the thing that has been mentioned: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
