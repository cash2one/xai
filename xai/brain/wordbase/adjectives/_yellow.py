

#calss header
class _YELLOW():
	def __init__(self,): 
		self.name = "YELLOW"
		self.definitions = [u'of a colour like that of a lemon or gold or the sun: ', u'belonging to a race that has pale yellowish-brown skin', u'easily frightened and not brave']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
