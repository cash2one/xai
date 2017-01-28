

#calss header
class _CIRCUMSTANTIAL():
	def __init__(self,): 
		self.name = "CIRCUMSTANTIAL"
		self.definitions = [u'containing information, especially about a crime, that makes you think something is true but does not completely prove it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
