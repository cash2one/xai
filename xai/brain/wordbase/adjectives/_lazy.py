

#calss header
class _LAZY():
	def __init__(self,): 
		self.name = "LAZY"
		self.definitions = [u'not willing to work or use any effort: ', u'slow and relaxed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
