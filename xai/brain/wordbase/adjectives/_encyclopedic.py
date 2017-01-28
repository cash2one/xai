

#calss header
class _ENCYCLOPEDIC():
	def __init__(self,): 
		self.name = "ENCYCLOPEDIC"
		self.definitions = [u'containing a lot of information', u'covering a large range of knowledge, often in great detail: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
