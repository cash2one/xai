

#calss header
class _ACRIMONIOUS():
	def __init__(self,): 
		self.name = "ACRIMONIOUS"
		self.definitions = [u'full of anger, arguments, and bad feeling: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
