

#calss header
class _ICY():
	def __init__(self,): 
		self.name = "ICY"
		self.definitions = [u'covered in ice: ', u'extremely cold: ', u'unfriendly and showing no emotion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
