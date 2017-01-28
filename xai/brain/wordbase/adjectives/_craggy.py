

#calss header
class _CRAGGY():
	def __init__(self,): 
		self.name = "CRAGGY"
		self.definitions = [u'having many crags: ', u"used to describe a man's face that is quite roughly formed and has loose skin but is also attractive: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
