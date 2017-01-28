

#calss header
class _TRIUMPHANT():
	def __init__(self,): 
		self.name = "TRIUMPHANT"
		self.definitions = [u'having achieved a great victory (= winning a war or competition) or success, or feeling very happy and proud because of such an achievement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
