

#calss header
class _VAGUE():
	def __init__(self,): 
		self.name = "VAGUE"
		self.definitions = [u'not clearly expressed, known, described, or decided: ', u'not clear in shape, or not clearly seen: ', u'A vague person is not able to think clearly, or gives an impression of not thinking clearly in order to hide their real thoughts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
