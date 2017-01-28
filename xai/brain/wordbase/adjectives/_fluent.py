

#calss header
class _FLUENT():
	def __init__(self,): 
		self.name = "FLUENT"
		self.definitions = [u'When a person is fluent, they can speak a language easily, well, and quickly: ', u'When a language is fluent, it is spoken easily and without many pauses: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
