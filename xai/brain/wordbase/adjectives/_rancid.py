

#calss header
class _RANCID():
	def __init__(self,): 
		self.name = "RANCID"
		self.definitions = [u'(of butter, oil, etc.) tasting or smelling unpleasant because of not being fresh']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
