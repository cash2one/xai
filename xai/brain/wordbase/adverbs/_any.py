

#calss header
class _ANY():
	def __init__(self,): 
		self.name = "ANY"
		self.definitions = [u'some, or even the smallest amount or number of: ', u'one of or each of a particular type of person or thing when it is not important which: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
