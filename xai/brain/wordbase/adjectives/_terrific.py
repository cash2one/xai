

#calss header
class _TERRIFIC():
	def __init__(self,): 
		self.name = "TERRIFIC"
		self.definitions = [u'very good: ', u'used to emphasize the great amount or degree of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
