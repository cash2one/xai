

#calss header
class _INCORRUPTIBLE():
	def __init__(self,): 
		self.name = "INCORRUPTIBLE"
		self.definitions = [u'morally strong enough not to be persuaded to do something wrong: ', u'If something is incorruptible, it will not decay or be destroyed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
