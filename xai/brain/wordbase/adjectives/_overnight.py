

#calss header
class _OVERNIGHT():
	def __init__(self,): 
		self.name = "OVERNIGHT"
		self.definitions = [u'for or during the night: ', u'suddenly and unexpectedly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
