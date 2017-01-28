

#calss header
class _FAMOUS():
	def __init__(self,): 
		self.name = "FAMOUS"
		self.definitions = [u'known and recognized by many people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
