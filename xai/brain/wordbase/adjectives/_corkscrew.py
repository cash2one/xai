

#calss header
class _CORKSCREW():
	def __init__(self,): 
		self.name = "CORKSCREW"
		self.definitions = [u'tightly twisted or curled: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
