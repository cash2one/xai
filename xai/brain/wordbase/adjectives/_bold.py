

#calss header
class _BOLD():
	def __init__(self,): 
		self.name = "BOLD"
		self.definitions = [u'not frightened of danger: ', u'strong in colour or shape, and very noticeable to the eye: ', u'printed in thick dark letters: ', u'not shy, especially in a way that shows no respect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
