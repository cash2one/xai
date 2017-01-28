

#calss header
class _SINCERELY():
	def __init__(self,): 
		self.name = "SINCERELY"
		self.definitions = [u'honestly and without pretending or lying: ', u'used to end a formal letter that is sent to a particular person']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
