

#calss header
class _SEATED():
	def __init__(self,): 
		self.name = "SEATED"
		self.definitions = [u'sitting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
