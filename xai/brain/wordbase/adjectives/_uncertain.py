

#calss header
class _UNCERTAIN():
	def __init__(self,): 
		self.name = "UNCERTAIN"
		self.definitions = [u'not knowing what to do or believe, or not able to decide about something: ', u'not known or fixed, or not completely certain: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
