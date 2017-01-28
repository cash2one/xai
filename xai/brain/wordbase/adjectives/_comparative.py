

#calss header
class _COMPARATIVE():
	def __init__(self,): 
		self.name = "COMPARATIVE"
		self.definitions = [u'comparing different things: ', u'a situation that is comfortable, free, silent, etc. when compared to another situation or what is normal: ', u'relating to the form of an adjective or adverb that expresses a difference in amount, number, degree, or quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
