

#calss header
class _SWAMPY():
	def __init__(self,): 
		self.name = "SWAMPY"
		self.definitions = [u'Swampy land is soft and very wet.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
