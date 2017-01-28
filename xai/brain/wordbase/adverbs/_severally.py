

#calss header
class _SEVERALLY():
	def __init__(self,): 
		self.name = "SEVERALLY"
		self.definitions = [u'separately, rather than as a member of a group: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
