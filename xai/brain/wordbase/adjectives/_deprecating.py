

#calss header
class _DEPRECATING():
	def __init__(self,): 
		self.name = "DEPRECATING"
		self.definitions = [u'showing that you think something is of little value or importance: ', u'showing that you feel embarrassed, especially by praise: ', u'showing that you do not approve of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
