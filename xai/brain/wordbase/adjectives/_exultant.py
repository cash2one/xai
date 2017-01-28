

#calss header
class _EXULTANT():
	def __init__(self,): 
		self.name = "EXULTANT"
		self.definitions = [u"very happy, especially at someone else's defeat or failure: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
