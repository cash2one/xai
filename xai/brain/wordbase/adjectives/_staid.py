

#calss header
class _STAID():
	def __init__(self,): 
		self.name = "STAID"
		self.definitions = [u'serious, boring, and slightly old-fashioned: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
