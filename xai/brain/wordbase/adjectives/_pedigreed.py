

#calss header
class _PEDIGREED():
	def __init__(self,): 
		self.name = "PEDIGREED"
		self.definitions = [u'used to describe an animal, especially a dog, whose parents and other relations are all of the same breed: ', u'from a family of high social class: ', u'having a lot of experience or a good reputation in a particular activity or job: ', u'from somewhere that you know and trust: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
