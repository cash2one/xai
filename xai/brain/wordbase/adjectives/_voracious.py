

#calss header
class _VORACIOUS():
	def __init__(self,): 
		self.name = "VORACIOUS"
		self.definitions = [u'very eager for something, especially a lot of food: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
