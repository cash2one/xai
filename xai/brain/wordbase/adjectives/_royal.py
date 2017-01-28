

#calss header
class _ROYAL():
	def __init__(self,): 
		self.name = "ROYAL"
		self.definitions = [u'belonging or connected to a king or queen or a member of their family: ', u'good or excellent, as if intended for or typical of royalty: ', u'big or great: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
