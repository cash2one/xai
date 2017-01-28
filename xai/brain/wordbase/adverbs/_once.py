

#calss header
class _ONCE():
	def __init__(self,): 
		self.name = "ONCE"
		self.definitions = [u'one single time: ', u'at the same time: ', u'used when something happens that does not usually happen: ', u'used to say that you will only do or request something on this particular occasion: ', u'again, as has happened before: ', u'one more time: ', u'again, as has happened before: ', u'a few times: ', u'sometimes but not often: ', u'completely and in a way that will finally solve a problem: ', u"only likely to happen once in a person's life: ", u'on a single occasion: ', u'in the past, but not now: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
