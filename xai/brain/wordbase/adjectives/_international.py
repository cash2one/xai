

#calss header
class _INTERNATIONAL():
	def __init__(self,): 
		self.name = "INTERNATIONAL"
		self.definitions = [u'involving more than one country: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
