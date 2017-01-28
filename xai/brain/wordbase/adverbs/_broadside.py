

#calss header
class _BROADSIDE():
	def __init__(self,): 
		self.name = "BROADSIDE"
		self.definitions = [u'with a side facing something : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
