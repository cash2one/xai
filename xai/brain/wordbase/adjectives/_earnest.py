

#calss header
class _EARNEST():
	def __init__(self,): 
		self.name = "EARNEST"
		self.definitions = [u'serious and determined, especially too serious and unable to find your own actions funny: ', u'completely serious: ', u'When something begins in earnest, it has already started but is now being done in a serious and complete way: ', u'to be speaking honestly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
