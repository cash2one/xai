

#calss header
class _DIAPHANOUS():
	def __init__(self,): 
		self.name = "DIAPHANOUS"
		self.definitions = [u'A diaphanous substance, especially cloth, is so delicate and thin that you can see through it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
