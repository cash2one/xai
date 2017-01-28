

#calss header
class _ANYWAY():
	def __init__(self,): 
		self.name = "ANYWAY"
		self.definitions = [u'whatever else is happening, without considering other things: ', u'In conversation, anyway is also used to change the subject, return to an earlier subject, or get to the most interesting point: ', u'used to give a more important reason for something that you are saying: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
