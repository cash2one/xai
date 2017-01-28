

#calss header
class _FOXY():
	def __init__(self,): 
		self.name = "FOXY"
		self.definitions = [u'like a fox in appearance', u'good at deceiving people', u'sexually attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
