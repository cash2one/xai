

#calss header
class _WRINKLED():
	def __init__(self,): 
		self.name = "WRINKLED"
		self.definitions = [u'(of skin) having small lines because of old age : ', u'(of cloth) having small lines or folds in it']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
