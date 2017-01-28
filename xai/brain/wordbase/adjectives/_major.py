

#calss header
class _MAJOR():
	def __init__(self,): 
		self.name = "MAJOR"
		self.definitions = [u'more important, bigger, or more serious than others of the same type: ', u'belonging or relating to a musical scale that is generally thought to have a happy sound: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
