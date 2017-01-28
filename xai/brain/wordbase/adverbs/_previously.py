

#calss header
class _PREVIOUSLY():
	def __init__(self,): 
		self.name = "PREVIOUSLY"
		self.definitions = [u'before the present time or the time referred to: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
