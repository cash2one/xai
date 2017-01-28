

#calss header
class _THEN():
	def __init__(self,): 
		self.name = "THEN"
		self.definitions = [u'next or after that: ', u'in addition: ', u'as a result; in that case; also used as a way of joining a statement to an earlier piece of conversation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
