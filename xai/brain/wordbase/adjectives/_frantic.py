

#calss header
class _FRANTIC():
	def __init__(self,): 
		self.name = "FRANTIC"
		self.definitions = [u'almost out of control because of extreme emotion, such as worry: ', u'done or arranged in a hurry and a state of excitement or confusion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
