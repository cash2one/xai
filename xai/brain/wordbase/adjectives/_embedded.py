

#calss header
class _EMBEDDED():
	def __init__(self,): 
		self.name = "EMBEDDED"
		self.definitions = [u'fixed into the surface of something: ', u'If an emotion, opinion, etc. is embedded in someone or something, it is a very strong or important part of him, her, or it: ', u'An embedded journalist or reporter travels with and is protected by a unit of soldiers during a war.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
