

#calss header
class _UNCONVENTIONAL():
	def __init__(self,): 
		self.name = "UNCONVENTIONAL"
		self.definitions = [u'different from what is usual or from the way most people do things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
