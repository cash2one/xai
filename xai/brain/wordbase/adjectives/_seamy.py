

#calss header
class _SEAMY():
	def __init__(self,): 
		self.name = "SEAMY"
		self.definitions = [u'(of a situation) unpleasant because of a connection with dishonest behaviour, violence, and illegal sex: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
