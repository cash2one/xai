

#calss header
class _ANYMORE():
	def __init__(self,): 
		self.name = "ANYMORE"
		self.definitions = [u'If you do not do something or something does not happen anymore, you have stopped doing it or it does not now happen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
