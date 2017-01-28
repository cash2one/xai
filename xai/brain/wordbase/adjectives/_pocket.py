

#calss header
class _POCKET():
	def __init__(self,): 
		self.name = "POCKET"
		self.definitions = [u'used to describe something that is small enough to put in your pocket, or that you regularly carry in your pocket: ', u'smaller than usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
