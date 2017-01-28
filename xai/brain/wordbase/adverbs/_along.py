

#calss header
class _ALONG():
	def __init__(self,): 
		self.name = "ALONG"
		self.definitions = [u'moving forward: ', u'with you: ', u'in addition to someone or something else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
