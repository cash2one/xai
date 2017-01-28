

#calss header
class _FORWARD():
	def __init__(self,): 
		self.name = "FORWARD"
		self.definitions = [u'towards the direction that is in front of you: ', u'towards the future: ', u'after that point: ', u'used in expressions related to progress: ', u'used, especially in business, to mean "in the future": ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
