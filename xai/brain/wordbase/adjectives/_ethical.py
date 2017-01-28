

#calss header
class _ETHICAL():
	def __init__(self,): 
		self.name = "ETHICAL"
		self.definitions = [u'relating to beliefs about what is morally right and wrong: ', u'morally right: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
