

#calss header
class _INVIDIOUS():
	def __init__(self,): 
		self.name = "INVIDIOUS"
		self.definitions = [u'likely to cause unhappiness or be unpleasant, especially because it is unfair: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
