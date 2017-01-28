

#calss header
class _SHOCKINGLY():
	def __init__(self,): 
		self.name = "SHOCKINGLY"
		self.definitions = [u'in a way that is offensive, upsetting, or immoral: ', u'in a way that is extremely bad or unpleasant, or of very low quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
