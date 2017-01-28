

#calss header
class _ACTING():
	def __init__(self,): 
		self.name = "ACTING"
		self.definitions = [u'someone who does a job for a short time while the person who usually does that job is not there: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
