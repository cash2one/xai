

#calss header
class _FOLLOWING():
	def __init__(self,): 
		self.name = "FOLLOWING"
		self.definitions = [u'The following day, morning, etc. is the next one.', u'a wind that is blowing in the same direction as the one in which you are going']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
