

#calss header
class _INFLECTED():
	def __init__(self,): 
		self.name = "INFLECTED"
		self.definitions = [u'An inflected form of a word has a changed spelling or ending that shows the way it is used in sentences: ', u'slightly changed by the influence of a particular thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
