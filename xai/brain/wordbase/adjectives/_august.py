

#calss header
class _AUGUST():
	def __init__(self,): 
		self.name = "AUGUST"
		self.definitions = [u'having great importance and especially of the highest social class: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
