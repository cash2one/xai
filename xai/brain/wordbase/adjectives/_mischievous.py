

#calss header
class _MISCHIEVOUS():
	def __init__(self,): 
		self.name = "MISCHIEVOUS"
		self.definitions = [u'behaving in a way, or describing behaviour, that is slightly bad but is not intended to cause serious harm or damage: ', u'expressing or suggesting mischief: ', u'used to describe behaviour or words that are intended to cause harm or trouble: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
