

#calss header
class _UNSUSPECTED():
	def __init__(self,): 
		self.name = "UNSUSPECTED"
		self.definitions = [u'not known or thought to exist: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
