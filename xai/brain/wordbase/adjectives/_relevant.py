

#calss header
class _RELEVANT():
	def __init__(self,): 
		self.name = "RELEVANT"
		self.definitions = [u'connected with what is happening or being discussed: ', u'correct or suitable for a particular purpose: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
