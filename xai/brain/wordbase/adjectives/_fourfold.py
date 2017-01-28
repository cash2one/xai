

#calss header
class _FOURFOLD():
	def __init__(self,): 
		self.name = "FOURFOLD"
		self.definitions = [u'four times as big or as much: ', u'having four parts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
