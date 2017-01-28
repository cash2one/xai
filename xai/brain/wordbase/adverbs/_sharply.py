

#calss header
class _SHARPLY():
	def __init__(self,): 
		self.name = "SHARPLY"
		self.definitions = [u'quickly and suddenly: ', u'in a way that will cut or make a hole: ', u'severely and angrily: ', u'clearly and obviously: ', u'in a fashionable way: ', u'quickly noticing things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
