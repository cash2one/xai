

#calss header
class _MATERIALLY():
	def __init__(self,): 
		self.name = "MATERIALLY"
		self.definitions = [u'in a way that relates to money and possessions: ', u'in an important or noticeable way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
