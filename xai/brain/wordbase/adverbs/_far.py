

#calss header
class _FAR():
	def __init__(self,): 
		self.name = "FAR"
		self.definitions = [u'at, to, or from a great distance in space or time: ', u'used to say what you think is true, although you do not know all the facts: ', u'used to say what your personal opinion is about something: ', u'used to say what you have noticed or understood: ', u'I certainly would not: ', u'certainly not something: ', u'used to describe something that is almost the opposite of something else: ', u'certainly not: ', u'from a large number of places: ', u'to be willing to do something that is extreme: ', u'until now: ', u'used to say that an activity has gone well until now: ', u'very much: ', u'by a great amount: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
