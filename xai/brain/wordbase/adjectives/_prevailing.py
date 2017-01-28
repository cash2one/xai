

#calss header
class _PREVAILING():
	def __init__(self,): 
		self.name = "PREVAILING"
		self.definitions = [u'existing in a particular place or at a particular time: ', u'a wind that usually blows in a particular direction: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
