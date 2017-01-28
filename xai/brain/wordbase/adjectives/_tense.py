

#calss header
class _TENSE():
	def __init__(self,): 
		self.name = "TENSE"
		self.definitions = [u'nervous and worried and unable to relax: ', u'If a situation is tense, it causes feelings of worry or nervousness: ', u'(of your body or part of the body) stretched tight and stiff', u'(of a speech sound) made with more force than other speech sounds']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
