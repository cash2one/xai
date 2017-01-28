

#calss header
class _HOKEY():
	def __init__(self,): 
		self.name = "HOKEY"
		self.definitions = [u'too emotional or artificial and therefore difficult to believe: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
