

#calss header
class _VIOLENTLY():
	def __init__(self,): 
		self.name = "VIOLENTLY"
		self.definitions = [u'in a forceful way that causes people to be hurt: ', u'strongly or extremely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
