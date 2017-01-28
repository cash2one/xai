

#calss header
class _GAMY():
	def __init__(self,): 
		self.name = "GAMY"
		self.definitions = [u'having the strong smell or taste of  game noun  (= wild animals or birds that are killed to eat)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
