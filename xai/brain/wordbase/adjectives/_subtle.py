

#calss header
class _SUBTLE():
	def __init__(self,): 
		self.name = "SUBTLE"
		self.definitions = [u'not loud, bright, noticeable, or obvious in any way: ', u'small but important: ', u'achieved in a quiet way that does not attract attention to itself and is therefore good or clever: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
