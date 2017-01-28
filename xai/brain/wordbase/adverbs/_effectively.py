

#calss header
class _EFFECTIVELY():
	def __init__(self,): 
		self.name = "EFFECTIVELY"
		self.definitions = [u'in a way that is successful and achieves what you want: ', u'used when you describe what the real result of a situation is: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
