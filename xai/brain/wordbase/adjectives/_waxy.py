

#calss header
class _WAXY():
	def __init__(self,): 
		self.name = "WAXY"
		self.definitions = [u'slightly shiny; looking like wax']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
