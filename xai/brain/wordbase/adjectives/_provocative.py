

#calss header
class _PROVOCATIVE():
	def __init__(self,): 
		self.name = "PROVOCATIVE"
		self.definitions = [u'causing thought about interesting subjects: ', u'causing an angry reaction, usually intentionally: ', u'If behaviour or clothing is provocative, it is intended to cause sexual desire: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
