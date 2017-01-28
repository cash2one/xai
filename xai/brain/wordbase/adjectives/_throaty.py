

#calss header
class _THROATY():
	def __init__(self,): 
		self.name = "THROATY"
		self.definitions = [u'A throaty sound is low and rough: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
