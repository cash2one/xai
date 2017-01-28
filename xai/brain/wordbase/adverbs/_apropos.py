

#calss header
class _APROPOS():
	def __init__(self,): 
		self.name = "APROPOS"
		self.definitions = [u'used to introduce something that is related to or connected with something that has just been said: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
