

#calss header
class _NEBULOUS():
	def __init__(self,): 
		self.name = "NEBULOUS"
		self.definitions = [u'(especially of ideas) not clear and having no form: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
