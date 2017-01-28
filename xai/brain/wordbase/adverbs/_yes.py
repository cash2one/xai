

#calss header
class _YES():
	def __init__(self,): 
		self.name = "YES"
		self.definitions = [u'used to express willingness or agreement: ', u'used for emphasis: ', u'used to show that you are listening to someone, or that you are ready to listen and to give them an answer or information: ', u'used when you are disagreeing with a negative statement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
