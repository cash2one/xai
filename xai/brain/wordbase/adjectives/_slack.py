

#calss header
class _SLACK():
	def __init__(self,): 
		self.name = "SLACK"
		self.definitions = [u'not tight; loose: ', u'showing little activity; not busy or happening in a positive way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
