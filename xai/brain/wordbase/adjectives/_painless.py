

#calss header
class _PAINLESS():
	def __init__(self,): 
		self.name = "PAINLESS"
		self.definitions = [u'causing no physical pain: ', u'causing no problems: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
