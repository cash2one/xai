

#calss header
class _INVERSE():
	def __init__(self,): 
		self.name = "INVERSE"
		self.definitions = [u'opposite in relation to something else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
