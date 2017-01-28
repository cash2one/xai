

#calss header
class _VALIANT():
	def __init__(self,): 
		self.name = "VALIANT"
		self.definitions = [u'very brave or bravely determined, especially when things are difficult or the situation gives no cause for hope: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
