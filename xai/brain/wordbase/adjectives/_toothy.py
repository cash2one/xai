

#calss header
class _TOOTHY():
	def __init__(self,): 
		self.name = "TOOTHY"
		self.definitions = [u'showing a lot of teeth when you smile: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
