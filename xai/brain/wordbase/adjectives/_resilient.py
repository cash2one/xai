

#calss header
class _RESILIENT():
	def __init__(self,): 
		self.name = "RESILIENT"
		self.definitions = [u'able to quickly return to a previous good condition: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
