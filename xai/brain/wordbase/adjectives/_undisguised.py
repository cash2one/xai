

#calss header
class _UNDISGUISED():
	def __init__(self,): 
		self.name = "UNDISGUISED"
		self.definitions = [u'An undisguised feeling is clearly shown or expressed, when it is usually kept hidden: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
