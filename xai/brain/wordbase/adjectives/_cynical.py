

#calss header
class _CYNICAL():
	def __init__(self,): 
		self.name = "CYNICAL"
		self.definitions = [u'believing that people are only interested in themselves and are not sincere: ', u"used to say that someone's feelings or emotions are used to your own advantage: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
