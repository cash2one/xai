

#calss header
class _BLINDLY():
	def __init__(self,): 
		self.name = "BLINDLY"
		self.definitions = [u'not able to see or not noticing what is around you: ', u'not thinking about or understanding what you are doing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
