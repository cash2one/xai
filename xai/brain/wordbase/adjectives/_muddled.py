

#calss header
class _MUDDLED():
	def __init__(self,): 
		self.name = "MUDDLED"
		self.definitions = [u'badly organized or confusing: ', u'A person who is muddled is confused: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
