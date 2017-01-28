

#calss header
class _PROMISING():
	def __init__(self,): 
		self.name = "PROMISING"
		self.definitions = [u'Something that is promising shows signs that it is going to be successful or enjoyable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
