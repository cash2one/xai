

#calss header
class _LATERALLY():
	def __init__(self,): 
		self.name = "LATERALLY"
		self.definitions = [u'towards the side', u'in a direction away from the midline: ', u'with the flow of air blocked in the middle, so that the air flows to the side: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
