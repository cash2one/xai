

#calss header
class _PRIOR():
	def __init__(self,): 
		self.name = "PRIOR"
		self.definitions = [u'existing or happening before something else, or before a particular time: ', u'before a particular time or event: ', u'more important: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
