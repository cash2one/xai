

#calss header
class _DELIRIOUS():
	def __init__(self,): 
		self.name = "DELIRIOUS"
		self.definitions = [u'unable to think or speak clearly because of fever or mental confusion: ', u'extremely happy or excited: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
