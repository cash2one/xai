

#calss header
class _CENSORIOUS():
	def __init__(self,): 
		self.name = "CENSORIOUS"
		self.definitions = [u'often criticizing other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
