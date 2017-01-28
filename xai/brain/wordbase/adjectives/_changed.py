

#calss header
class _CHANGED():
	def __init__(self,): 
		self.name = "CHANGED"
		self.definitions = [u'someone whose behaviour and character has changed a lot, especially improved: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
