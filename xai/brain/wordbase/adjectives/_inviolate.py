

#calss header
class _INVIOLATE():
	def __init__(self,): 
		self.name = "INVIOLATE"
		self.definitions = [u'(that must be) not harmed or damaged: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
