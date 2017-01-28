

#calss header
class _FRUSTRATED():
	def __init__(self,): 
		self.name = "FRUSTRATED"
		self.definitions = [u'feeling annoyed or less confident because you cannot achieve what you want: ', u'used to say that a person who has not succeeded in a particular type of job: ', u'A frustrated emotion is one that you are not able to express: ', u'unhappy because you are not having as much sex as you want']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
