

#calss header
class _LAUGHINGLY():
	def __init__(self,): 
		self.name = "LAUGHINGLY"
		self.definitions = [u'If you do something laughingly, you are laughing while you are doing it: ', u'If you say something is laughingly described in a particular way, you think this thing is so bad that it does not deserve the description: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
