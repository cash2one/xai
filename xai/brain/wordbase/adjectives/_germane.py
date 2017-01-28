

#calss header
class _GERMANE():
	def __init__(self,): 
		self.name = "GERMANE"
		self.definitions = [u'Ideas or information that is germane to a particular subject or situation is is connected with and important to it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
