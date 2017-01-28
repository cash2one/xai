

#calss header
class _FAITHLESS():
	def __init__(self,): 
		self.name = "FAITHLESS"
		self.definitions = [u'not loyal and not able to be trusted', u'not faithful sexually to your marriage partner or usual sexual partner: ', u'with no religious faith']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
