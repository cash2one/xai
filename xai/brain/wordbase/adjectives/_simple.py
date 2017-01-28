

#calss header
class _SIMPLE():
	def __init__(self,): 
		self.name = "SIMPLE"
		self.definitions = [u'easy to understand or do; not difficult: ', u'used to describe the one important fact, truth, etc.: ', u'without decoration; plain: ', u'having or made of only one or a few parts: ', u'ordinary; traditional or natural rather than modern and complicated: ', u'A simple person does not have a normal level of intelligence: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
