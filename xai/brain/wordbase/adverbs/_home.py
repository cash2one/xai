

#calss header
class _HOME():
	def __init__(self,): 
		self.name = "HOME"
		self.definitions = [u'at or to your house or the place where you live: ', u'in or to the country or area where you come from: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
