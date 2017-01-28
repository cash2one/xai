

#calss header
class _PAINFUL():
	def __init__(self,): 
		self.name = "PAINFUL"
		self.definitions = [u'causing emotional or physical pain: ', u'If something is painful to watch or listen to, it is so bad that it makes you feel embarrassed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
