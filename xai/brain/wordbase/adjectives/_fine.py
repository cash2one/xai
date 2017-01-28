

#calss header
class _FINE():
	def __init__(self,): 
		self.name = "FINE"
		self.definitions = [u'good or good enough; healthy and well: ', u'excellent or much better than average: ', u'very thin or in very small pieces or drops: ', u'very exact and delicate, or needing to be done, treated, or considered very carefully: ', u'sunny and dry: ', u'bad or not convenient: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
