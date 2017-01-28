

#calss header
class _DEPENDENT():
	def __init__(self,): 
		self.name = "DEPENDENT"
		self.definitions = [u'needing the support of something or someone in order to continue existing or operating: ', u'influenced or decided by something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
