

#calss header
class _IMMEASURABLE():
	def __init__(self,): 
		self.name = "IMMEASURABLE"
		self.definitions = [u'so large or great that it cannot be measured or known exactly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
