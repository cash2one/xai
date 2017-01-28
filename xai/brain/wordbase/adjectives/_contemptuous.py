

#calss header
class _CONTEMPTUOUS():
	def __init__(self,): 
		self.name = "CONTEMPTUOUS"
		self.definitions = [u'expressing contempt: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
