

#calss header
class _UNAPPEALING():
	def __init__(self,): 
		self.name = "UNAPPEALING"
		self.definitions = [u'not attractive or interesting']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
