

#calss header
class _UNFAVOURABLE():
	def __init__(self,): 
		self.name = "UNFAVOURABLE"
		self.definitions = [u'not giving you an advantage or a good chance of success: ', u'negative and showing that you do not like something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
