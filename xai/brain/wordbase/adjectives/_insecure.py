

#calss header
class _INSECURE():
	def __init__(self,): 
		self.name = "INSECURE"
		self.definitions = [u'Insecure people have little confidence and are uncertain about their own abilities or if other people really like them: ', u'(of objects or situations) not safe or not protected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
