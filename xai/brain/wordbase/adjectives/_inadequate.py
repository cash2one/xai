

#calss header
class _INADEQUATE():
	def __init__(self,): 
		self.name = "INADEQUATE"
		self.definitions = [u'not good enough or too low in quality: ', u'too small in amount: ', u'not confident enough to deal with a situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
