

#calss header
class _SINCE():
	def __init__(self,): 
		self.name = "SINCE"
		self.definitions = [u'from a particular time in the past until a later time, or until now: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
