

#calss header
class _HOMEGROWN():
	def __init__(self,): 
		self.name = "HOMEGROWN"
		self.definitions = [u'from your own garden: ', u'If someone or something is homegrown, he, she, or it belongs to or was developed in your own country: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
