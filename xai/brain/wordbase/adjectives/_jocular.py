

#calss header
class _JOCULAR():
	def __init__(self,): 
		self.name = "JOCULAR"
		self.definitions = [u'funny or intended to make someone laugh: ', u'used to describe someone who is happy and likes to make jokes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
