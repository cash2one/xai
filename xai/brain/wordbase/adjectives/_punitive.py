

#calss header
class _PUNITIVE():
	def __init__(self,): 
		self.name = "PUNITIVE"
		self.definitions = [u'intended as a punishment: ', u'used to describe costs that are so high they are difficult to pay: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
