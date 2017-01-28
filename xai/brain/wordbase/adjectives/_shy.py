

#calss header
class _SHY():
	def __init__(self,): 
		self.name = "SHY"
		self.definitions = [u'nervous and uncomfortable with other people: ', u'less than: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
