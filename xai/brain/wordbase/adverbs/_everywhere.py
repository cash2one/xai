

#calss header
class _EVERYWHERE():
	def __init__(self,): 
		self.name = "EVERYWHERE"
		self.definitions = [u'to, at, or in all places or the whole of a place: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
