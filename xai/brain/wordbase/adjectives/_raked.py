

#calss header
class _RAKED():
	def __init__(self,): 
		self.name = "RAKED"
		self.definitions = [u'sloping: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
