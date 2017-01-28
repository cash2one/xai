

#calss header
class _MANIFEST():
	def __init__(self,): 
		self.name = "MANIFEST"
		self.definitions = [u'easily noticed or obvious: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
