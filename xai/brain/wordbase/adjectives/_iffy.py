

#calss header
class _IFFY():
	def __init__(self,): 
		self.name = "IFFY"
		self.definitions = [u'not certain or decided: ', u'not completely good, honest, or suitable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
