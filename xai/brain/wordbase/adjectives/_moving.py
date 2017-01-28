

#calss header
class _MOVING():
	def __init__(self,): 
		self.name = "MOVING"
		self.definitions = [u'A moving object is one that moves: ', u'causing strong feelings of sadness or sympathy: ', u'causing someone to take action: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
