

#calss header
class _BOUNCY():
	def __init__(self,): 
		self.name = "BOUNCY"
		self.definitions = [u'able to bounce: ', u'happy and energetic: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
