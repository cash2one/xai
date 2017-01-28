

#calss header
class _HYPOALLERGENIC():
	def __init__(self,): 
		self.name = "HYPOALLERGENIC"
		self.definitions = [u'designed to be less likely to cause allergic reactions (= physical problems caused by particular substances) in people who use a product: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
