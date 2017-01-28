

#calss header
class _TOLERANT():
	def __init__(self,): 
		self.name = "TOLERANT"
		self.definitions = [u'willing to accept behaviour and beliefs that are different from your own, although you might not agree with or approve of them: ', u'able to deal with something unpleasant or annoying, or to continue existing despite bad or difficult conditions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
