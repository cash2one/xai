

#calss header
class _UNCOMMUNICATIVE():
	def __init__(self,): 
		self.name = "UNCOMMUNICATIVE"
		self.definitions = [u'not willing to talk: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
