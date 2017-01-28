

#calss header
class _UNRESERVED():
	def __init__(self,): 
		self.name = "UNRESERVED"
		self.definitions = [u'without any doubts or feeling uncertain; total: ', u'An unreserved seat, ticket, etc. is not being kept for a particular person to use: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
