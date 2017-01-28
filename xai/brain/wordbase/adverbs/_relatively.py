

#calss header
class _RELATIVELY():
	def __init__(self,): 
		self.name = "RELATIVELY"
		self.definitions = [u'quite good, bad, etc. in comparison with other similar things or with what you expect: ', u'said when you are judging one thing in comparison with other things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
