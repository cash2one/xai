

#calss header
class _POSTHUMOUS():
	def __init__(self,): 
		self.name = "POSTHUMOUS"
		self.definitions = [u"happening after a person's death: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
