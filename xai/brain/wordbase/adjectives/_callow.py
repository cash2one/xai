

#calss header
class _CALLOW():
	def __init__(self,): 
		self.name = "CALLOW"
		self.definitions = [u'Someone, especially a young person, who is callow behaves in a way that shows they have little experience, confidence, or judgment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
