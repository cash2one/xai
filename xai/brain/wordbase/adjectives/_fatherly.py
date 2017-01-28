

#calss header
class _FATHERLY():
	def __init__(self,): 
		self.name = "FATHERLY"
		self.definitions = [u'used to describe a man or male behaviour typical of a kind and loving father: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
