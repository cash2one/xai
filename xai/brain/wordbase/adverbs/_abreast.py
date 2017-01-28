

#calss header
class _ABREAST():
	def __init__(self,): 
		self.name = "ABREAST"
		self.definitions = [u'used to say that two or more people are next to each other and moving in the same direction: ', u'to make sure you know all the most recent facts about a subject or situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
