

#calss header
class _UNQUENCHABLE():
	def __init__(self,): 
		self.name = "UNQUENCHABLE"
		self.definitions = [u'used for describing a feeling that is so strong that it cannot be satisfied: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
