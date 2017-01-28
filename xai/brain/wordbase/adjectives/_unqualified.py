

#calss header
class _UNQUALIFIED():
	def __init__(self,): 
		self.name = "UNQUALIFIED"
		self.definitions = [u'An unqualified person does not have the qualifications needed for a particular job.', u'not limited in any way; to the largest degree possible: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
