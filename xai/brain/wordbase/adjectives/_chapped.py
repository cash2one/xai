

#calss header
class _CHAPPED():
	def __init__(self,): 
		self.name = "CHAPPED"
		self.definitions = [u'Chapped skin is sore, rough, and broken, especially because of cold weather: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
