

#calss header
class _ANNOYED():
	def __init__(self,): 
		self.name = "ANNOYED"
		self.definitions = [u'angry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
