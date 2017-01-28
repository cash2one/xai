

#calss header
class _DIRECT():
	def __init__(self,): 
		self.name = "DIRECT"
		self.definitions = [u'going in a straight line towards somewhere or someone without stopping or changing direction: ', u'without anyone or anything else being involved or between: ', u'strong light or heat that has nothing protecting and separating you from it: ', u'a relation who is related to you through one of your parents, not through an aunt or uncle, etc.: ', u'complete: ', u"Someone who is direct says what they think in a very honest way without worrying about other people's opinions: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
