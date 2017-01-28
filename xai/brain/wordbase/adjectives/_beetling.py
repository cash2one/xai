

#calss header
class _BEETLING():
	def __init__(self,): 
		self.name = "BEETLING"
		self.definitions = [u'beetling eyebrows are thick and stick out from the face: ', u'a beetling rock or hill sticks out over things below it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
