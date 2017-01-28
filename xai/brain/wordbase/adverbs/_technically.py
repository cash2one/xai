

#calss header
class _TECHNICALLY():
	def __init__(self,): 
		self.name = "TECHNICALLY"
		self.definitions = [u'according to an exact understanding of rules, facts, etc.: ', u'in a way that relates to the knowledge, machines, or methods used in science and industry: ', u'in a way that relates to practical skills and methods that are used in a particular activity: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
