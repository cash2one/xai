

#calss header
class _REACTIVE():
	def __init__(self,): 
		self.name = "REACTIVE"
		self.definitions = [u'reacting to events or situations rather than acting first to change or prevent something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
