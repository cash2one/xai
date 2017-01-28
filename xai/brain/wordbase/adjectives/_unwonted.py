

#calss header
class _UNWONTED():
	def __init__(self,): 
		self.name = "UNWONTED"
		self.definitions = [u'unusual; not often experienced or shown: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
