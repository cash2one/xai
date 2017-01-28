

#calss header
class _MISCONCEIVED():
	def __init__(self,): 
		self.name = "MISCONCEIVED"
		self.definitions = [u'badly planned because of a failure to understand a situation and therefore unsuitable or unlikely to succeed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
