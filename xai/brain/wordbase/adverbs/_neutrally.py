

#calss header
class _NEUTRALLY():
	def __init__(self,): 
		self.name = "NEUTRALLY"
		self.definitions = [u'in a way that does not encourage or support any of the groups involved in something and does not show personal opinion: ', u'using colours such as white, cream, and grey: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
