

#calss header
class _LEGISLATIVE():
	def __init__(self,): 
		self.name = "LEGISLATIVE"
		self.definitions = [u'relating to laws or the making of laws: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
