

#calss header
class _BACKWARD():
	def __init__(self,): 
		self.name = "BACKWARD"
		self.definitions = [u'not advanced: ', u'towards the direction that is the opposite to the one in which you are facing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
