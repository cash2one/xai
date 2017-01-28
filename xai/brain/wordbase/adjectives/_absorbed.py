

#calss header
class _ABSORBED():
	def __init__(self,): 
		self.name = "ABSORBED"
		self.definitions = [u'very interested in something and not paying attention to anything else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
