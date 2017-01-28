

#calss header
class _DETRIMENTAL():
	def __init__(self,): 
		self.name = "DETRIMENTAL"
		self.definitions = [u'causing harm or damage: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
