

#calss header
class _WRETCHEDLY():
	def __init__(self,): 
		self.name = "WRETCHEDLY"
		self.definitions = [u'extremely, when referring to something unpleasant or of low quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
