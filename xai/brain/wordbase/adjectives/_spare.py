

#calss header
class _SPARE():
	def __init__(self,): 
		self.name = "SPARE"
		self.definitions = [u'If something is spare, it is available to use because it is extra: ', u'time when you are not working: ', u'tall and thin: ', u'plain and not decorated: ', u'to get very upset or angry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
