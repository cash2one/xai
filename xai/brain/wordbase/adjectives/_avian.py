

#calss header
class _AVIAN():
	def __init__(self,): 
		self.name = "AVIAN"
		self.definitions = [u'of or relating to birds']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
