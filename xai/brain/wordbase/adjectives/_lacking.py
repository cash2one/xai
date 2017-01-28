

#calss header
class _LACKING():
	def __init__(self,): 
		self.name = "LACKING"
		self.definitions = [u'If something that you need is lacking, you do not have enough of it: ', u'to not have a quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
