

#calss header
class _MOBILE():
	def __init__(self,): 
		self.name = "MOBILE"
		self.definitions = [u'moving or walking around freely: ', u'able to be moved from one place to another: ', u'used to describe a service available on a mobile phone, small computer, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
