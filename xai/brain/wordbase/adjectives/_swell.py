

#calss header
class _SWELL():
	def __init__(self,): 
		self.name = "SWELL"
		self.definitions = [u'very good or pleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
