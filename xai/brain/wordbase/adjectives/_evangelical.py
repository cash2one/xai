

#calss header
class _EVANGELICAL():
	def __init__(self,): 
		self.name = "EVANGELICAL"
		self.definitions = [u'belonging to one of the Protestant Churches or Christian groups that believe the teaching of the Bible and persuading other people to join them to be extremely important: ', u'having very strong beliefs and often trying to persuade other people to have the same beliefs: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
