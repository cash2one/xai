

#calss header
class _OTIOSE():
	def __init__(self,): 
		self.name = "OTIOSE"
		self.definitions = [u'used to describe a word or phrase, or sometimes an idea, that is unnecessary or has been used several times: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
