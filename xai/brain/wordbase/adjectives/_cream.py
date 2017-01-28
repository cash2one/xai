

#calss header
class _CREAM():
	def __init__(self,): 
		self.name = "CREAM"
		self.definitions = [u'having a yellowish-white colour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
