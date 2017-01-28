

#calss header
class _IRRECOVERABLE():
	def __init__(self,): 
		self.name = "IRRECOVERABLE"
		self.definitions = [u'impossible to get back: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
