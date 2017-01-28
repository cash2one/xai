

#calss header
class _ENSUING():
	def __init__(self,): 
		self.name = "ENSUING"
		self.definitions = [u'happening after something and because of it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
