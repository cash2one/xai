

#calss header
class _SWIFT():
	def __init__(self,): 
		self.name = "SWIFT"
		self.definitions = [u'happening or moving quickly or within a short time, especially in a smooth and easy way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
