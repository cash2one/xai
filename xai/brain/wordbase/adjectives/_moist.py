

#calss header
class _MOIST():
	def __init__(self,): 
		self.name = "MOIST"
		self.definitions = [u'slightly wet, especially in a good way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
