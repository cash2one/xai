

#calss header
class _INTOXICATING():
	def __init__(self,): 
		self.name = "INTOXICATING"
		self.definitions = [u'If a drink is intoxicating, it makes you drunk if you have too much: ', u'An intoxicating experience or idea makes you feel excited and emotional: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
