

#calss header
class _INTUITIVE():
	def __init__(self,): 
		self.name = "INTUITIVE"
		self.definitions = [u'based on feelings rather than facts or proof: ', u'able to know or understand something because of feelings rather than facts or proof: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
