

#calss header
class _UNLICENSED():
	def __init__(self,): 
		self.name = "UNLICENSED"
		self.definitions = [u'not having a licence (= a document giving legal permission) to do something, for example to sell alcohol, or use or own something, for example a gun: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
