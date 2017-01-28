

#calss header
class _NEGLIGIBLE():
	def __init__(self,): 
		self.name = "NEGLIGIBLE"
		self.definitions = [u'too slight or small in amount to be of importance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
