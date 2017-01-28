

#calss header
class _PREDATORY():
	def __init__(self,): 
		self.name = "PREDATORY"
		self.definitions = [u'A predatory animal kills and eats other animals: ', u'A predatory person or organization tries to get something that belongs to someone else: ', u'used to describe someone who expresses sexual interest in a very obvious way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
