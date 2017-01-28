

#calss header
class _QUIET():
	def __init__(self,): 
		self.name = "QUIET"
		self.definitions = [u'making very little noise: ', u'having little activity or excitement and few people: ', u'A quiet person is one who does not talk much: ', u'to try to stop other people from finding out about a fact: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
