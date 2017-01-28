

#calss header
class _CLEVERLY():
	def __init__(self,): 
		self.name = "CLEVERLY"
		self.definitions = [u'in a clever or skilful way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
