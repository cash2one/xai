

#calss header
class _MALIGN():
	def __init__(self,): 
		self.name = "MALIGN"
		self.definitions = [u'causing or intending to cause harm or evil: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
