

#calss header
class _MERCURIAL():
	def __init__(self,): 
		self.name = "MERCURIAL"
		self.definitions = [u'changing suddenly and often: ', u'intelligent, enthusiastic, and quick: ', u'containing or caused by mercury: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
