

#calss header
class _ARRESTING():
	def __init__(self,): 
		self.name = "ARRESTING"
		self.definitions = [u'very attractive in a way that attracts a lot of attention: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
