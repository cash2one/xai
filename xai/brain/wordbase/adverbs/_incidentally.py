

#calss header
class _INCIDENTALLY():
	def __init__(self,): 
		self.name = "INCIDENTALLY"
		self.definitions = [u'used before saying something that is not as important as the main subject of conversation, but is connected to it in some way: ', u'used when mentioning a subject that has not been discussed before, often making it seem less important than it really is: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
