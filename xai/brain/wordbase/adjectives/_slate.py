

#calss header
class _SLATE():
	def __init__(self,): 
		self.name = "SLATE"
		self.definitions = [u'of a colour similar to slate: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
