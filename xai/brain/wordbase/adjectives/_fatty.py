

#calss header
class _FATTY():
	def __init__(self,): 
		self.name = "FATTY"
		self.definitions = [u'containing a lot of fat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
