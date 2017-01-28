

#calss header
class _SHORT():
	def __init__(self,): 
		self.name = "SHORT"
		self.definitions = [u'before the arranged or expected time or place: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
