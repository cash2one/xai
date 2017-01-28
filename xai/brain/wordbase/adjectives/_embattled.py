

#calss header
class _EMBATTLED():
	def __init__(self,): 
		self.name = "EMBATTLED"
		self.definitions = [u'having a lot of problems or difficulties: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
