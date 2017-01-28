

#calss header
class _UNTOUCHABLE():
	def __init__(self,): 
		self.name = "UNTOUCHABLE"
		self.definitions = [u'not able to be punished, criticized, or changed in any way: ', u'not able to be defeated or to be as good as: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
