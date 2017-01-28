

#calss header
class _SLIGHTLY():
	def __init__(self,): 
		self.name = "SLIGHTLY"
		self.definitions = [u'a little: ', u'Someone who is slightly built is thin and delicate.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
