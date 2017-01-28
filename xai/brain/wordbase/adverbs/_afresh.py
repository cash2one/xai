

#calss header
class _AFRESH():
	def __init__(self,): 
		self.name = "AFRESH"
		self.definitions = [u'If you do something afresh, you deal with it again in a new way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
