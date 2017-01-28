

#calss header
class _PREFERENTIAL():
	def __init__(self,): 
		self.name = "PREFERENTIAL"
		self.definitions = [u'used to say that something you are given that is better than what other people receive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
