

#calss header
class _ISOLATED():
	def __init__(self,): 
		self.name = "ISOLATED"
		self.definitions = [u'not near to other places: ', u'happening or existing only once, separate: ', u'feeling unhappy because of not seeing or talking to other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
