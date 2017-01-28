

#calss header
class _CORDIAL():
	def __init__(self,): 
		self.name = "CORDIAL"
		self.definitions = [u'friendly, but formal and polite: ', u'(of a feeling, especially dislike) strong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
