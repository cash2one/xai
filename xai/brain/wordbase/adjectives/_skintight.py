

#calss header
class _SKINTIGHT():
	def __init__(self,): 
		self.name = "SKINTIGHT"
		self.definitions = [u'Skintight clothes fit tightly around the body: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
