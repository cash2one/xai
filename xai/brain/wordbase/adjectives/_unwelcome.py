

#calss header
class _UNWELCOME():
	def __init__(self,): 
		self.name = "UNWELCOME"
		self.definitions = [u'not wanted: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
