

#calss header
class _NEEDFUL():
	def __init__(self,): 
		self.name = "NEEDFUL"
		self.definitions = [u'necessary: ', u'needing something: ', u'to do what is necessary in a situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
