

#calss header
class _FINISHED():
	def __init__(self,): 
		self.name = "FINISHED"
		self.definitions = [u'completed, final or completely used : ', u'having completed a particular task, or stopped using something: ', u'not able to continue, after a failure of some kind: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
