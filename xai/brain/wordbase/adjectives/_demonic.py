

#calss header
class _DEMONIC():
	def __init__(self,): 
		self.name = "DEMONIC"
		self.definitions = [u'wild and evil: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
