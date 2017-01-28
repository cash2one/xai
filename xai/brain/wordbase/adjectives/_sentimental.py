

#calss header
class _SENTIMENTAL():
	def __init__(self,): 
		self.name = "SENTIMENTAL"
		self.definitions = [u'A sentimental person is strongly influenced by emotional feelings, especially about happy memories of past events or relationships with other people, rather than by careful thought and judgment based on facts: ', u'too strongly influenced by emotional feelings: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
