

#calss header
class _STIMULATING():
	def __init__(self,): 
		self.name = "STIMULATING"
		self.definitions = [u'If something is stimulating, it encourages new ideas: ', u'A stimulating person makes you feel enthusiastic and full of ideas: ', u'If an activity is stimulating, it causes your body to be active: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
