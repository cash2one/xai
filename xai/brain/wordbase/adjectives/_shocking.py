

#calss header
class _SHOCKING():
	def __init__(self,): 
		self.name = "SHOCKING"
		self.definitions = [u'offensive, upsetting, or immoral: ', u'extremely bad or unpleasant, or of very low quality: ', u'extremely surprising: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
