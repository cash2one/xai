

#calss header
class _DAZED():
	def __init__(self,): 
		self.name = "DAZED"
		self.definitions = [u'very confused and unable to think clearly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
