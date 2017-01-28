

#calss header
class _MERRILY():
	def __init__(self,): 
		self.name = "MERRILY"
		self.definitions = [u'showing happiness or enjoyment: ', u'without thinking about the result of what you are doing or about the problems it might cause: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
