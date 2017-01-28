

#calss header
class _VULGAR():
	def __init__(self,): 
		self.name = "VULGAR"
		self.definitions = [u'not suitable, simple, dignified or beautiful; not in the style preferred by the upper classes of society: ', u'rude and likely to upset or anger people, especially by referring to sex and the body in an unpleasant way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
