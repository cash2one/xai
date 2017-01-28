

#calss header
class _SHARP():
	def __init__(self,): 
		self.name = "SHARP"
		self.definitions = [u'suddenly or immediately: ', u'exactly at the stated time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
