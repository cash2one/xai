

#calss header
class _SPANKING():
	def __init__(self,): 
		self.name = "SPANKING"
		self.definitions = [u'very quick: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
