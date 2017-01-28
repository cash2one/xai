

#calss header
class _TEMPORARY():
	def __init__(self,): 
		self.name = "TEMPORARY"
		self.definitions = [u'not lasting or needed for very long: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
