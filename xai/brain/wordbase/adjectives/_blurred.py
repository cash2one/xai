

#calss header
class _BLURRED():
	def __init__(self,): 
		self.name = "BLURRED"
		self.definitions = [u'difficult to see: ', u'difficult to understand or separate clearly: ', u'unable to see clearly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
