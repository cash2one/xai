

#calss header
class _SUNNI():
	def __init__(self,): 
		self.name = "SUNNI"
		self.definitions = [u'(a member) of the largest Islamic religious group, which follows the teachings only of Mohammed, not those of any of the religious leaders who came after him: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
