

#calss header
class _JOBBING():
	def __init__(self,): 
		self.name = "JOBBING"
		self.definitions = [u'someone who does not work regularly for one person or organization but does small pieces of work for different people']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
