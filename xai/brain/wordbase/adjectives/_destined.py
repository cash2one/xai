

#calss header
class _DESTINED():
	def __init__(self,): 
		self.name = "DESTINED"
		self.definitions = [u'intended (for a particular purpose): ', u'travelling or being sent to somewhere: ', u'controlled by fate, and not by humans: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
