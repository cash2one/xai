

#calss header
class _THIS():
	def __init__(self,): 
		self.name = "THIS"
		self.definitions = [u'used for a person, object, idea, etc. to show which one is referred to: ', u'used when you introduce someone to someone else: ', u'already: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
