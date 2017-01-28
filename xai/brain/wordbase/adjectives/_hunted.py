

#calss header
class _HUNTED():
	def __init__(self,): 
		self.name = "HUNTED"
		self.definitions = [u'looking frightened and worried: ', u'A hunted animal or person is being chased by someone.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
