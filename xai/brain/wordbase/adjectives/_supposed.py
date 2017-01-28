

#calss header
class _SUPPOSED():
	def __init__(self,): 
		self.name = "SUPPOSED"
		self.definitions = [u'to have to; to have a duty or a responsibility to: ', u'to be intended to: ', u'used to show that you do not believe that something or someone really is what many other people consider them to be: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
