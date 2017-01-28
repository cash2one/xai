

#calss header
class _NEWFANGLED():
	def __init__(self,): 
		self.name = "NEWFANGLED"
		self.definitions = [u'recently made for the first time, but not always an improvement on what existed before: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
