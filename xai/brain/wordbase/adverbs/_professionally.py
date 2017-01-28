

#calss header
class _PROFESSIONALLY():
	def __init__(self,): 
		self.name = "PROFESSIONALLY"
		self.definitions = [u'by people with particular skills or qualifications: ', u'as a paid job, not as a hobby: ', u'as a person with a particular job: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
