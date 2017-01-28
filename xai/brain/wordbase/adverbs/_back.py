

#calss header
class _BACK():
	def __init__(self,): 
		self.name = "BACK"
		self.definitions = [u'in, into, or towards a previous place or condition, or an earlier time: ', u'in return: ', u'in reply: ', u'further away in distance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
