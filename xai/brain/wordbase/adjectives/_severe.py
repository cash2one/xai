

#calss header
class _SEVERE():
	def __init__(self,): 
		self.name = "SEVERE"
		self.definitions = [u'causing very great pain, difficulty, worry, damage, etc.; very serious: ', u'extreme or very difficult: ', u"not kind or showing sympathy; not willing to accept other people's mistakes or failures: ", u'completely plain and without decoration: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
