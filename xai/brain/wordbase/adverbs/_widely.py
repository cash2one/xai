

#calss header
class _WIDELY():
	def __init__(self,): 
		self.name = "WIDELY"
		self.definitions = [u'including a lot of different places, people, subjects, etc.: ', u'to be very different: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
