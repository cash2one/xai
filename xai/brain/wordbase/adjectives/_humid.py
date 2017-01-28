

#calss header
class _HUMID():
	def __init__(self,): 
		self.name = "HUMID"
		self.definitions = [u'(of air and weather conditions) containing extremely small drops of water in the air: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
