

#calss header
class _STUBBY():
	def __init__(self,): 
		self.name = "STUBBY"
		self.definitions = [u'short and thick: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
