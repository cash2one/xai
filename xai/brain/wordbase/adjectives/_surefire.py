

#calss header
class _SUREFIRE():
	def __init__(self,): 
		self.name = "SUREFIRE"
		self.definitions = [u'certain or likely, especially to succeed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
