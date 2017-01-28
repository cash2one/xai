

#calss header
class _DIRECT():
	def __init__(self,): 
		self.name = "DIRECT"
		self.definitions = [u'without having to stop or change direction: ', u'without anything or anyone else being involved or in between: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
