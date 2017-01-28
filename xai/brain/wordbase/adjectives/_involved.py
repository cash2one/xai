

#calss header
class _INVOLVED():
	def __init__(self,): 
		self.name = "INVOLVED"
		self.definitions = [u'not simple and therefore difficult to understand: ', u'being in a close relationship with someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
