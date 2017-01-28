

#calss header
class _SCATTERED():
	def __init__(self,): 
		self.name = "SCATTERED"
		self.definitions = [u'covering a wide area: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
