

#calss header
class _REFLECTIVE():
	def __init__(self,): 
		self.name = "REFLECTIVE"
		self.definitions = [u'A reflective surface sends back most of the light that shines on it and can therefore be seen easily.', u'thinking carefully and quietly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
