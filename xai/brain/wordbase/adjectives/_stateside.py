

#calss header
class _STATESIDE():
	def __init__(self,): 
		self.name = "STATESIDE"
		self.definitions = [u'related to the US; in or towards the US: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
