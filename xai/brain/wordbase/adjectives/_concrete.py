

#calss header
class _CONCRETE():
	def __init__(self,): 
		self.name = "CONCRETE"
		self.definitions = [u'clear and certain, or real and existing in a form that can be seen or felt: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
