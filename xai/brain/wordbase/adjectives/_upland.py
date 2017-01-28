

#calss header
class _UPLAND():
	def __init__(self,): 
		self.name = "UPLAND"
		self.definitions = [u'An upland area of land is high up, such as on a hill or mountain: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
