

#calss header
class _LOVESICK():
	def __init__(self,): 
		self.name = "LOVESICK"
		self.definitions = [u'sad because the person you love does not love you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
